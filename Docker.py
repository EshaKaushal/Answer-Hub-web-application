FROM python:3.7-slim

EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY Streamlitapp.py /app/Streamlitapp.py

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "/app/Streamlitapp.py"]
