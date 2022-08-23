FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install netcat -y

RUN apt-get update -y && apt-get install -y postgresql gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /usr/src/app

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


#COPY entrypoint.sh ./entrypoint.sh
#RUN chmod +x /entrypoint.sh

#RUN chmod +x app/entrypoint.sh

#COPY ./entrypoint.sh /usr/src/kinocms/
#RUN ["chmod", "+x", "/usr/src/kinocms/entrypoint.sh"]
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

#ENTRYPOINT ["/usr/src/kinocms/entrypoint.sh"]
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]