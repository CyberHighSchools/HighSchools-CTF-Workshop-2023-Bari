FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt --no-warn-script-location

RUN python3 app.py
CMD ["uwsgi", "--http", ":5000", "--wsgi-file", "app.py", "--callable", "app", "--thunder-lock", "--enable-threads"]
