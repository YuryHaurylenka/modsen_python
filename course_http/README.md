# Requests to OpenWeather API


# EN

This project is designed to work with the OpenWeather API and includes functionality for retrieving response statuses and weather information for a specific city.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/YuryHaurylenka/modsen.git
    cd modsen
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your API key:
    ```env
    CORRECT_API_KEY=your_correct_api_key
    ```

## Running the Server

1. Navigate to the directory containing your FastAPI application `course_http`:
    ```sh
    cd course_http
    ```

2. Start the server using Uvicorn:
    ```sh
    uvicorn main:app --reload
    ```

    You should see the following output if the server starts successfully:
    ```sh
    INFO:     Will watch for changes in these directories: ['/path/to/your/project']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [pid] using WatchFiles
    INFO:     Started server process [pid]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

## Using the API

1. Get all statuses:
    ```sh
    GET /statuses
    ```

    This endpoint returns the statuses of various requests to the OpenWeather API.

2. Get weather for a specific city:
    ```sh
    GET /weather/{city}
    ```

    Example request:
    ```sh
    GET /weather/Minsk
    ```

    This endpoint returns the current weather for the specified city.

## Test Cases

The `/statuses` endpoint checks the following cases:

- Correct API key and city name
- Incorrect API key
- Missing city name
- Incorrect city name
- Invalid coordinates (latitude and longitude)
- Valid coordinates (latitude and longitude)
- Correct API key and another valid city name
- Empty city name
- City name with numbers

## Requirements

- Python 3.7+
- FastAPI
- httpx
- python-dotenv
- Uvicorn


# RU

Этот проект предназначен для работы с OpenWeather API и включает функциональность для получения статусов ответов и информации о погоде для определенного города.

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/YuryHaurylenka/modsen.git
    cd modsen
    ```

2. Создайте и активируйте виртуальное окружение:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корневой директории проекта и добавьте ваш API ключ:
    ```env
    CORRECT_API_KEY=ваш_api_ключ
    ```

## Запуск сервера

1. Перейдите в директорию, содержащую ваше приложение FastAPI `course_http`:
    ```sh
    cd course_http
    ```

2. Запустите сервер, используя Uvicorn:
    ```sh
    uvicorn main:app --reload
    ```

    Если сервер запустился успешно, вы увидите следующий вывод:
    ```sh
    INFO:     Will watch for changes in these directories: ['/path/to/your/project']
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [pid] using WatchFiles
    INFO:     Started server process [pid]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```

## Использование API

1. Получить все статусы:
    ```sh
    GET /statuses
    ```

    Этот эндпоинт возвращает статусы различных запросов к OpenWeather API.

2. Получить погоду для конкретного города:
    ```sh
    GET /weather/{city}
    ```

    Пример запроса:
    ```sh
    GET /weather/Minsk
    ```

    Этот эндпоинт возвращает текущую погоду для указанного города.

## Тестовые случаи

Эндпоинт `/statuses` проверяет следующие случаи:

- Правильный API ключ и название города
- Неправильный API ключ
- Отсутствие названия города
- Неправильное название города
- Неверные координаты (широта и долгота)
- Верные координаты (широта и долгота)
- Правильный API ключ и другое правильное название города
- Пустое название города
- Название города с цифрами

## Требования

- Python 3.7+
- FastAPI
- httpx
- python-dotenv
- Uvicorn

