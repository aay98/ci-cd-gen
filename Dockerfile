FROM python:3.12.0b3-bullseye
WORKDIR /app
COPY . .
EXPOSE 555
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python3", "app.py"]

