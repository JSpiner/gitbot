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
        wget \
        openssh-client \
        software-properties-common 

# Install gradle
RUN add-apt-repository ppa:cwchien/gradle
RUN apt-get update
RUN apt-get install gradle

# Install Java
RUN apt-add-repository ppa:openjdk-r/ppa
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk

# Export JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

# Install Android SDK
RUN wget https://dl.google.com/android/android-sdk_r24.4.1-linux.tgz
RUN tar -xvzf android-sdk_r24.4.1-linux.tgz
RUN mv android-sdk-linux /usr/local/android-sdk
RUN rm android-sdk_r24.4.1-linux.tgz

ENV ANDROID_COMPONENTS platform-tools,android-26,build-tools-25.0.3,build-tools-26.0.1,extra-google-m2repository,extra-android-m2repository

# Install Android tools
RUN echo y | /usr/local/android-sdk/tools/android update sdk --filter "${ANDROID_COMPONENTS}" --no-ui -a

# Environment variables
ENV ANDROID_HOME /usr/local/android-sdk
ENV ANDROID_SDK_HOME $ANDROID_HOME
ENV ANDROID_NDK_HOME /usr/local/android-ndk
ENV PATH $PATH:$ANDROID_SDK_HOME/tools
ENV PATH $PATH:$ANDROID_SDK_HOME/platform-tools
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/23.0.2
ENV PATH $PATH:$ANDROID_SDK_HOME/build-tools/24.0.0
ENV PATH $PATH:$ANDROID_NDK_HOME