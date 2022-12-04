FROM python:3.8-slim

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY ./src/ /app/
COPY Pipfile /app/
COPY Pipfile.lock /app/

RUN pip3 install pipenv
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
