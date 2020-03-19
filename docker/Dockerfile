FROM ubuntu:18.04
RUN apt update && apt install -y python3.8 \
python3.8-dev \
git \
python3-pip \
default-libmysqlclient-dev
RUN python3.8 -m pip install Django==3.0.3 mysqlclient
CMD git clone https://github.com/MikhaelMIEM/free_chan ~/free_chan && \
python3.8 ~/free_chan/manage.py makemigrations && \
python3.8 ~/free_chan/manage.py migrate && \
python3.8 ~/free_chan/manage.py runserver 0:80
