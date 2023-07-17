FROM python:3.10

RUN apt update
RUN pip install -qq -U pip poetry==1.1.15
WORKDIR /opt/esdv_web
RUN mkdir /opt/esdv_web/static_root
RUN mkdir /opt/esdv_web/media_root
COPY . .
RUN poetry install

CMD poetry run python manage.py migrate --no-input; \
    poetry run python manage.py collectstatic --no-input; \
    poetry run python manage.py compress --force

