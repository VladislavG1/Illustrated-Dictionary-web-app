FROM python:3.12.2
ENV PYTHONUNBUFFERED 1
ARG HTTP_PROXY

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --proxy $HTTP_PROXY --upgrade pip && pip install --proxy $HTTP_PROXY --no-cache-dir -r requirements.txt

COPY App /app/
