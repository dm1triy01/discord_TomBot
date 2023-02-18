FROM debian:bullseye-20221024
LABEL maintainer="dm1triy01"
RUN apt update
RUN apt install python3 && apt install python3-pip
RUN pip install --user -r requirements.txt
COPY . ./discord/bots/tom
CMD python3 /discord/bots/tom/bot.py