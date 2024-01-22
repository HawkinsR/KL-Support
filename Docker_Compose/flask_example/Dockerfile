FROM python:3.9
WORKDIR /srv
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=app
CMD ["python", "app.py"]
