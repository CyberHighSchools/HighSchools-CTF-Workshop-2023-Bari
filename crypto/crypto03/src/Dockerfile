FROM alpine:latest

RUN apk add --update --no-cache python3 py-pip 
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8080

CMD ["python3", "./index.py"]