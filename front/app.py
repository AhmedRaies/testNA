from flask import Flask
from flask import render_template
app=Flask(__name__, template_folder='templates')


@app.route('/upload')
def upload_files():
   return render_template("form.html")


app.run(host="0.0.0.0", port=7000) 