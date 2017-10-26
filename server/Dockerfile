FROM python:3.6.1
MAINTAINER Patrick Ryan <pjryan126@gmail.com>

# Create the group and user to be used in this container
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

# Create the working directory (and set it as the working directory)
RUN mkdir -p /home/flask/project
WORKDIR /home/flask/project

# Install the package dependencies (this step is separated
# from copying all the source code to avoid having to
# re-install all python packages defined in requirements.txt
# whenever any source code change is made)
COPY ./project/requirements.txt /home/flask/project/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

# Copy the source code into the container
ADD project /home/flask/project/

RUN chmod +x manage.py

RUN chown -R flask:flaskgroup /home/flask

USER flask