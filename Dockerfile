FROM python:3.8
LABEL MAINTAINER="Mehran Saadat | @mehransdt"
ENV PYTHONUNBUFFERED 1
RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

ADD requirments/requirments.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requirments.txt

RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "blogpy", "--bind", ":8000", "blogpy.wsgi:application"]

