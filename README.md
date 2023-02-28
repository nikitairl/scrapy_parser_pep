### Scrappy PEP parser - Асинхронный парсер PEP-документов и информации о них на базе фреймворка Scrapy.
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-3D550C?style=flat-square&logo=Scrapy)](https://scrapy.org/)

## Основная информация о проекте:
Парсер собирает информацию о PEP с следующего адреса: [peps.python.org](https://peps.python.org/)

Собираемая информация:
| number                | name | status |
|:---------------------:| ----:| ------:|
|                       |      |        |

Собираемая информация сохраняется в .csv файл.

## Инструкция по установке.
# Установка

После загрузки проекта на свою машину, разверните виртуальное окружение:

```
python -m venv venv
```
Активируйте виртуальное окружение:
Windows:
```
. venv/Scripts/activate
```
Mac:
```
. venv/bin/activate
```
Установите последнюю версию Pip:
```
python3 -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
# Использование
Для запуска парсера используйте следующую команду:
```
scrapy crawl pep
```
