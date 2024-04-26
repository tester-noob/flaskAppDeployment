FROM python:3.9

WORKDIR /app

RUN pip install Flask

COPY . /app

CMD ["python","app.py"]