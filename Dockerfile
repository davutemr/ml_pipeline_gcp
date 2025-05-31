FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app/ app/
copy model/ model/

EXPOSE 5000

CMD ["python", "main.py"]

