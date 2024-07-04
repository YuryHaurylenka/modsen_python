# Selenium Automation Scripts

# EN

## Description 

This project contains two Python scripts that use the Selenium library to automate interaction with web pages. One script works with LocalStorage, and the other works with cookies.

## Installation

### Installing Selenium

To install the Selenium library, run the following command:

```sh
pip install selenium
```

### ChromeDriver installation

1. Download ChromeDriver с [официального сайта]().
2. Unzip the file and place it in a convenient location.
3. Add the ChromeDriver path to your system's PATH variable or specify the full path in the script.

## Scripts

### Local Storage

The local_storage_test.py script performs the following actions:

1. Opens a web page.
2. Sets a value in LocalStorage.
3. Retrieves and prints this value.
4. Removes the value from LocalStorage.
5. Verifies that the value has been removed.

### Cookies

The cookie.py script performs the following actions:

1. Opens a web page.
2. Sets a value in a cookie.
3. Retrieves and prints this value.
4. Removes the value from the cookie.
5. Verifies that the value has been removed.

## Running the scripts

Run each script with the command:
```sh
python local_storage_test.py
```

```sh
python cookie.py
```

# RU

## Описание

Этот проект 
содержит два скрипта на Python, которые используют библиотеку Selenium для автоматизации взаимодействия с веб-страницами. Один скрипт работает с LocalStorage, а другой — с cookies.

## Установка

### Установка Selenium

Для установки библиотеки Selenium выполните следующую команду:

```sh
pip install selenium
```

### Установка ChromeDriver

1. Скачайте ChromeDriver с [официального сайта]().
2. Распакуйте файл и поместите его в удобное для вас место.
3. Добавьте путь к ChromeDriver в переменную PATH вашей системы или укажите полный путь в скрипте.

## Скрипты

### Local Storage

Скрипт local_storage_test.py выполняет следующие действия:

1. Открывает веб-страницу.
2. Устанавливает значение в LocalStorage.
3. Получает и выводит это значение.
4. Удаляет значение из LocalStorage.
5. Проверяет, что значение удалено.

### Cookies

Скрипт cookie.py выполняет следующие действия:

1. Открывает веб-страницу.
2. Устанавливает значение в cookie.
3. Получает и выводит это значение.
4. Удаляет значение из cookie.
5. Проверяет, что значение удалено.

## Запуск скриптов

Запустите каждый скрипт командой 

```sh
python local_storage_test.py
```

```sh
python cookie.py
```