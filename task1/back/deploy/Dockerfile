FROM python:3.6-stretch

WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y libsndfile1-dev
RUN apt-get install -y ffmpeg

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
EXPOSE 8001

COPY . .

CMD ["python", "server.py"]

