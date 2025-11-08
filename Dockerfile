FROM python:3.13-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py /usr/src/app/

CMD ["python3", "main.py"]
