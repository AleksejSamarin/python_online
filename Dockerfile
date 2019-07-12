FROM python:3.7-alpine
COPY . /
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "flaskr/main.py" ]