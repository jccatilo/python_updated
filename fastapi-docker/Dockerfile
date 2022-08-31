# base image
FROM python:3.8

# i want to organize the folders in the container in a better way like creating a working directory. our docker file will automatically go to this working dir
WORKDIR /fastapi-app

#copy the requirements.txt file in the root to the working dir
COPY requirements.txt .

# run the copied requirements.txt
RUN pip install -r requirements.txt

# COPY <directory in our root> <directory in our container>
COPY ./app ./app

CMD ["python", "./app/main.py"]