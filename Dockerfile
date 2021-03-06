#first line is of the image I am going to be used to inherit the image from the dockerfile.. alpine means the light weight version of python
FROM python:3.7-alpine
# 2nd line is the maintainer the codebase and docker image of the develoer or the company name (It is optional)
MAINTAINER armanShanto the develoer of the company

#running the app without any buffer in the environment variables I want to set, it tells python to run unbuffered while running the project especially in docker container
ENV PYTHONUNBUFFERED 1

# first copy the requirements.txt file from the root directory and create a file in the docker container then run the requirements.txt file in the docker container.
COPY ./requirements.txt /requirements.txt
# Run the postgres client and then download the necessary dependencies while running the postgres client.
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-builds-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip3 install -r /requirements.txt
# after download the postgresql client with necessary dependencies then delete the dependencies running the command
RUN apk del .tmp-builds-deps

# first run a directory in the docker image then tells docker container that our main working directory is the /app level then copy our  local directory to docker container
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# create a user with a username for security purpose using adduser command user is the username here
RUN adduser -D user
RUN chown user:user -R /app/
RUN chmod +x /app
USER user


