FROM ubuntu:18.04

RUN : mkdir /app \
    && apt-get update -y \
    && apt-get install python3.8 -y \
    &&  apt-get install python3-pip -y \
    && apt-get install python3.8-dev -y \
    && apt-get install vim nano -y \
    # && update-alternatives  --set python /usr/bin/python3.8 \
    && :
    

COPY requirements.txt /app/
COPY app.py /app/app.py
COPY templates /app/templates
COPY Datasets /app/Datasets
COPY model /app/model
COPY predict /app/predict
COPY preprocessing /app/preprocessing

WORKDIR /app


# # RUN python3 -m venv $VIRTUAL_ENV
# # Activation of virtualenv
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN alias python3=/usr/bin/python3.8 \
    && apt-get install python3-venv -y

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip3 install --upgrade setuptools

RUN pip3 --no-cache-dir install -r requirements.txt \
    && pip3 install -U scikit-learn


SHELL [ "/bin/bash", "-c" ]
CMD ["python", "app.py", "/bin/bash" ]







# FROM ubuntu:bionic

# RUN : mkdir /app \
#     && apt-get update \
#     && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
#         software-properties-common \
#     && add-apt-repository -y ppa:deadsnakes \
#     && apt-get update && apt-get upgrade -y \
#     && apt-get install python3.8 -y \
#     && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
#         python3.8-venv \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/* \
#     && :

# COPY requirements.txt /app/
# COPY app.py /app/app.py
# COPY templates /app/templates
# COPY Datasets /app/Datasets
# COPY model /app/model
# COPY predict /app/predict
# COPY preprocessing /app/preprocessing

# WORKDIR /app
# RUN pip install -r requirements.txt #freeze requirements.txt

# SHELL [ "/bin/bash", "-c" ]
# CMD ["python", "app.py", "/bin/bash" ]


# RUN python3.8 -m venv /venv
# ENV PATH=/venv/bin:$PATH
