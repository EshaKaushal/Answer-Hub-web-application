FROM python:3.7

# Creating Application Source Code Directory
RUN mkdir -p /usr/src/app

# Setting Home Directory for containers
WORKDIR /usr/src/app

# Installing python dependencies
COPY requirements.txt .
RUN pip install  -r requirements.txt

# Copying src code to Container
COPY  . /usr/src/app
RUN chmod 777 -R *

EXPOSE 8080

# Running StreamLit Application
CMD streamlit run --server.port 8080 --server.enableCORS false /usr/src/app/Streamlitapp.py
