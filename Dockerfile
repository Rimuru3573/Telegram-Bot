FROM python:alpine

WORKDIR /app

RUN pip install aiogram
RUN pip install openai
RUN pip install aiohttp-socks

COPY get.py .
COPY main.py .

CMD ["python", "main.py"]

