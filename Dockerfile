FROM python:3.7.2-alpine3.9

# Set the working directory to /app
WORKDIR /appdown

# Copy the current directory contents into the container at /app
COPY . /appdown

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/
RUN rm /etc/apk/repositories && echo -e 'http://mirrors.ustc.edu.cn/alpine/v3.5/main\nhttp://mirrors.ustc.edu.cn/alpine/v3.5/community' > /etc/apk/repositories && apk update && apk add git \
    && git config --global user.name "yourname" && git config --global user.email "yourname@example.com"
# Define environment variable
# ENV NAME World

# Run app.py when the container launches
#CMD ["pytest", "./test_case"]
