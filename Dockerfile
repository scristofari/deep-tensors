FROM ubuntu:artful

RUN apt-get update && apt-get install python-pip python-dev python-virtualenv -y

RUN virtualenv --system-site-packages ~/tensorflow
RUN /bin/bash -c "source ~/tensorflow/bin/activate && pip install --upgrade tensorflow"

RUN echo 'source ~/tensorflow/bin/activate' >> ~/.bashrc

WORKDIR /root