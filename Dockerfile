FROM python:3.7-slim

EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

COPY requirements.txt . 

RUN pip install -r requirements.txt 

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "Streamlitapp.py"]
