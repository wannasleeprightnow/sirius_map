FROM python:3.11

RUN mkdir /code

WORKDIR /code

COPY . .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements/prod.txt

WORKDIR src

RUN alembic upgrade head

CMD gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000