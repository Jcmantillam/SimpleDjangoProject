FROM python:3.7

ENV PYTHONUNBUFFERED=1

ENV code_web_DIR=/code_web

RUN mkdir $code_web_DIR

WORKDIR $code_web_DIR

ADD requirements.txt $code_web_DIR/

RUN pip install -r requirements.txt

ADD . $code_web_DIR/
