# set the base image 
FROM python:3.10.7

ENV PYTHONUNBUFFERED=1

#add project files to the usr/src/app folder
ADD . /central/static

#set directoty where CMD will execute 
WORKDIR /central

COPY requirements.txt /central/

# Get pip to download and install requirements:
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000

COPY . /central/

# default command to execute    
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]