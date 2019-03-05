FROM rabbitmq:latest
LABEL version="0.1" maintainer='jjmerelo@gmail.com'

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-pip 
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1\
    && update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

ADD create-user-rmq.sh cliente-con-celery.py PlatziAgenda.py PlatziTareas.py SlackComandos.py PlatziSlack.py requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

RUN echo "127.0.0.1 localhost" > /etc/hosts \
    echo "127.0.1.1 platzi" >> /etc/hosts \
    echo "platzi" > /etc/hostname

CMD ./create-user-rmq.sh $RMQ_PASS &&  celery -A PlatziTareas worker --loglevel=info
