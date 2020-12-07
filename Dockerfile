FROM ubuntu:bionic

RUN : mkdir /app \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        software-properties-common \
    && add-apt-repository -y ppa:deadsnakes \
    && apt-get update && apt-get upgrade -y \
    && apt-get install python3.8 -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3.8-venv \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && :

COPY requirements.txt /app/
COPY app.py /app/app.py
COPY templates /app/templates
COPY Datasets /app/Datasets
COPY model /app/model
COPY predict /app/predict
COPY preprocessing /app/preprocessing

WORKDIR /app
RUN pip install -R requirements.txt #freeze requirements.txt

SHELL [ "/bin/bash", "-c" ]
CMD ["python", "app.py", "/bin/bash" ]


RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH
