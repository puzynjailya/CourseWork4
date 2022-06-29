FROM python:3.10-slim

LABEL maintainer='puzynjailya@gmail.com'

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP='run.py'
ENV FLASK_ENV='development'

#CMD flask run -h 0.0.0.0 -p 80

CMD ["sh","entrypoint.sh"]


