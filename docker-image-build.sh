#!/bin/sh

# Запросить у пользователя имя образа
read -p "Введите имя образа: " image_name

# Выполнить команду docker build
docker build -t "$image_name" .