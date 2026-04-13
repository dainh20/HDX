FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Cài system packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev \
    git \
    curl \
    vim \
    nano \
    iputils-ping \
    net-tools \
    redis-tools \
    postgresql-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Alias python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Upgrade pip + cài core libs
RUN pip install --upgrade pip && \
    pip install django psycopg2-binary redis

# Working directory
WORKDIR /app

# Tạo user (best practice)
RUN useradd -ms /bin/bash devuser
USER devuser

# Default: dev mode (không auto chạy)
CMD ["sleep", "infinity"]