# Docker file, Docker Image, Docker Container
# Docker file - a blue print for creating docker images
# Docker Image - template for running containers
# Docker Container - Actual running process

# Docker file
FROM python:3.8

# ADD <source file> <destination file> 
ADD main.py .
ADD requirements.txt .
RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]