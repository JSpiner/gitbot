FROM ubuntu:16.04

# Add ssh key
ADD .ssh/gitbot /root/.ssh/gitbot

# Add build script
ADD *.sh /root/

# Update apt-get
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get dist-upgrade -y

# Install packages
RUN apt-get install -y \
        git \
        openssh-client \
        software-properties-common

# Install Java
RUN apt-add-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk

# Export JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/