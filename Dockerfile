# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code
COPY . /code/
RUN pip install -r /code/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]