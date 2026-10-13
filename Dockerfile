FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install mne

CMD ["python", "main.py"]