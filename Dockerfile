FROM python:3.9

WORKDIR /app

COPY job-scaler.py /app

RUN pip install kubernetes

CMD ["python", "job-scaler.py"]
