FROM debian:bullseye-20221024
LABEL maintainer="dm1triy01"

RUN apt update; \
    apt install python3 python3-pip; \
    apt clean

COPY . ./root/bot/src/

WORKDIR /root/bot/src/

RUN pip install --user -r requirements.txt


CMD ["python3", "/root/bot/src/bot.py"]