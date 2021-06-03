FROM python:3.8-slim
COPY requirements.txt
COPY Streamlitapp.py /app/Streamlitapp.py
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "--server.port", "8080", "--server.enableCORS", "false", "/app/Streamlitapp.py"]
