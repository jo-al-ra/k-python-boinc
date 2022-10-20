FROM boinc/client:base-ubuntu

LABEL maintainer="JadenData" \
      description="Boinc client executing a minimal task in IExec container"

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 --no-cache-dir install -r requirements.txt
COPY ./src /app

ENTRYPOINT ["python3", "/app/template_app.py"]