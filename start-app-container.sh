#!/bin/sh

# Запросить у пользователя имя образа
read -p "Введите имя образа: " image_name

# Выполнить команду docker run
docker run -p 4000:80 "$image_name"