FROM tensorflow/tensorflow

EXPOSE 6000

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /back
COPY . .

#CMD ["cat","app.py"]

CMD ["python","app.py"]