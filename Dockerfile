FROM ubuntu:bionic

RUN : mkdir /app \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        software-properties-common \
    && add-apt-repository -y ppa:deadsnakes \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3.8-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

COPY requirements.txt /app/
COPY app.py /app/app.py
COPY templates /app/templates

WORKDIR /app

SHELL [ "/bin/bash", "-c" ]
CMD ["python", "app.py", "/bin/bash" ]


RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH