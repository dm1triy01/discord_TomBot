FROM python:3.10
LABEL maintainer="dm1triy01"
RUN pip install --user -r requirements.txt
COPY . ./app
ADD https://raw.githubusercontent.com/discdiver/pachy-vid/master/sample_vids/vid1.mp4 \
/my_app_directory
RUN ["mkdir", "/a_directory"]
CMD ["python", "./bot.py"]