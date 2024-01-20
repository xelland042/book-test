FROM python:3.11.7

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim


RUN useradd -rms /bin/bash user && chmod 777 /opt /run

WORKDIR /app

#RUN mkdir /app/static && mkdir /app/media && chown -R user /app && chmod 755 /app

COPY . .

RUN pip install -r requirements.txt


#CMD ["python3","manage.py", "runserver","0.0.0.0:8000"]