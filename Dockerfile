FROM python:3.8
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY ./app.py .
COPY ./models ./models
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
