FROM ubuntu:xenial

RUN apt-get update && apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose -y

RUN apt-get update && apt-get install python-pip python-dev python-virtualenv -y

RUN virtualenv --system-site-packages ~/tensorflow
RUN /bin/bash -c "source ~/tensorflow/bin/activate && pip install --upgrade tensorflow"

RUN echo 'source ~/tensorflow/bin/activate' >> ~/.bashrc

RUN apt-get install python-matplotlib

WORKDIR /root