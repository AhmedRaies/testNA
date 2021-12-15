import librosa
import pickle
import os.path

import librosa.display
import numpy as np

import os
from werkzeug.utils import secure_filename

from flask import Flask
from flask import render_template, request
app = Flask(__name__)

# Import the libraries

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'wav'}
#pp = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return "hello"
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'No file selected'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            signal, rate = librosa.load(UPLOAD_FOLDER+'/'+filename)
            # The Mel Spectrogram
            S = librosa.feature.melspectrogram(signal, sr=rate, n_fft=2048,    hop_length=512, n_mels=128)
            S_DB = librosa.power_to_db(S, ref=np.max)
            S_DB = S_DB.flatten()[:1200]
            clf = pickle.load(open('SVM.pkl', 'rb'))
            ans = clf.predict([S_DB])[0]
            music_class = str(ans)
            print(music_class)
            return music_class

app.run(host="0.0.0.0", port=6000)
