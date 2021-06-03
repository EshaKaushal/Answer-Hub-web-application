FROM python:3.8-slim
EXPOSE 8080
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "Streamlitapp.py"]
