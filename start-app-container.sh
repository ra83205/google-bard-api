#!/bin/sh

# Запросить у пользователя имя образа
read -p "Введите имя образа: " image_name

# Выполнить команду docker run
docker run -d -p 80:80 --name=my_app_container --restart=unless-stopped "$image_name"