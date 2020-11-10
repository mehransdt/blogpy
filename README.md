# blogpy
simple blog with django and python

Create network and volumes in docker with below commands:

$ docker volume create blogpy_postgresql
$ docker volume create blogpy_static_volume
$ docker volume create blogpy_files_volume
$ docker network create nginx_network
$ docker network create blogpy_network

create .env file in the project root with below values:

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres

run Django and postgresql by this command:

docker-compose up -u
