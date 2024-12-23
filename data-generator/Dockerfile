FROM python:3.9-slim

WORKDIR /app

RUN python -m venv venv && . venv/bin/activate \
    && pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY kdatagenerator.py .

EXPOSE 9092

CMD ["python3", "kdatagenerator.py"]
