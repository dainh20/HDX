FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

WORKDIR /hdx

# Install system dependencies
RUN apt update && apt install -y \
    openjdk-17-jdk \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    vim \
    postgresql-client \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && apt clean

# Install python dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    sqlalchemy \
    psycopg2-binary \
    passlib[bcrypt] \
    python-jose

CMD ["tail", "-f", "/dev/null"]