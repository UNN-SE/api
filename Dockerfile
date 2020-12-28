FROM python:3.9

RUN apt-get update \
  && apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    yasm \
    pkg-config \
    libswscale-dev \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libavformat-dev \
    libpq-dev \
  && rm -rf /var/lib/apt/lists/*

RUN pip install numpy

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

ENV NO_DB=false FLASK_ENV=production

CMD flask run --host=0.0.0.0

EXPOSE 5000
