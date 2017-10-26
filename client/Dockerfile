# Create image based on the official Node 6 image from dockerhub
FROM node:6
MAINTAINER Patrick Ryan <pjryan126@gmail.com>

# Create a directory where our app will be placed
RUN mkdir -p /usr/angular/project

# Change directory so that our commands run inside this new directory
WORKDIR /usr/angular/project

# Copy dependency definitions
ADD project /usr/angular/project/

# Install dependecies
RUN npm install