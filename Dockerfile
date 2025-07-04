FROM python:alpine

WORKDIR /app

RUN pip install aiogram
RUN pip install openai

COPY get.py .
COPY main.py .

CMD ["python", "main.py"]

