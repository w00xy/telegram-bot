FROM python:3.11.6-alpine

WORKDIR /bot
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /bot

CMD ["python", "main.py"]