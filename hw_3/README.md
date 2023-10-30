# docker_python_ngnix_gunicorn

## Сборка и запуск проекта:

`docker-compose up -d`

## Список сервисов:
`docker-compose ps --services`

## Логи сервиса (послед. 20 строк):
`docker logs --tail 20 <service>` 

## По умолчанию приложение запускается по адресу:
http://localhost:8082/
