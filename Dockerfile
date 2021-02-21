FROM alpine:3.7
COPY conf /tmp
RUN apk add python3 py3-pip python3-dev alpine-sdk
RUN pip3 install pandas 
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --no-cache-dir -U pip wheel setuptools
RUN apk update && apk upgrade
RUN apk add --update curl gcc g++
RUN pip3 install numpy
RUN apk add zlib jpeg-dev zlib-dev
RUN pip3 install --upgrade Pillow
RUN pip3 install -r /tmp/requirements.txt && \
   rm -rf /tmp/requirements.txt
RUN pip3 install boto3
RUN pip3 install fsspec
RUN pip3 install s3fs
WORKDIR /code
COPY src /code
CMD ["export", "FLASK_APP=app.py"]
CMD ["flask", "run", "--host=0.0.0.0"]






