# Requests to OpenWeatherMap API


# EN


## Description

This project demonstrates the usage of FastAPI to interact with the OpenWeatherMap API and obtain various response status codes. Different test cases are implemented to explore possible status codes and explain why some of them cannot be obtained.

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

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project's root directory and add your API key:
    ```
    CORRECT_API_KEY=your_api_key
    ```

## Running the Server

1. Navigate to the directory containing your FastAPI application `course_http`:
    ```sh
    cd course_http
    ```

2. Launch the server using Uvicorn:
    ```sh
    uvicorn main:app --reload
    ```

    If the server starts successfully, you will see the following output:
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

    This endpoint returns the statuses of various requests to the OpenWeatherMap API.

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

The `/statuses` endpoint tests the following cases:

- Correct API key and city name
- Incorrect API key
- Absence of city name
- Incorrect city name
- Invalid coordinates (latitude and longitude)
- Valid coordinates (latitude and longitude)
- Correct API key and another correct city name
- Empty city name
- City name with numbers
- Empty parameters
- Invalid `units` parameter value
- Latitude out of valid range
- Longitude out of valid range
- Invalid `cnt` parameter value
- City name with spaces
- Long non-existent city name
- Invalid `lang` parameter value

### Obtained Status Codes, Available with OpenWeatherMap Free Subscription

1. **200 OK**
   - Description: The request was successful, and the server returned the expected result.
   - Example: Correct API key and city name.

2. **401 Unauthorized**
   - Description: The request requires authentication. Typically, this means the API key is missing or incorrect.
   - Example: Incorrect API key or absent API key.

3. **404 Not Found**
   - Description: The requested resource was not found. This could mean the specified city does not exist.
   - Example: Incorrect city name.

4. **400 Bad Request**
   - Description: The server cannot process the request due to client error, such as invalid parameter values.
   - Example: Invalid coordinates, invalid parameter values (`units`, `cnt`, etc.).

5. **429 Too Many Requests**
   - Description: The request rate limit has been exceeded. This status code may be received if too many requests are sent in a short period.
   - Example: Exceeding API request limit (60 per minute).

## Status Codes Not Received

1. **500 Internal Server Error**
   - **Description:** This status code indicates a general server error. In the context of the OpenWeatherMap API, server errors are rare and were not encountered during testing.

2. **501 Not Implemented**
   - **Description:** This code indicates that the server does not support the functionality required to fulfill the request. All supported requests in the OpenWeatherMap API were successfully executed, and this status code was not received.
   - **Example:** Requesting functionality not implemented in the API.

3. **502 Bad Gateway**
   - **Description:** This status code indicates that the server, acting as a gateway or proxy, received an invalid response from an upstream server. Since the OpenWeatherMap API directly handles requests, this code was not received.
   - **Example:** Proxy server unable to get a valid response from the OpenWeatherMap server.

4. **503 Service Unavailable**
   - **Description:** This code indicates temporary unavailability of the service. OpenWeatherMap API has high availability, and the service was accessible during testing, so this status code was not received.
   - **Example:** Attempting to access the API during maintenance.

5. **504 Gateway Timeout**
   - **Description:** This status code indicates that the server, acting as a gateway or proxy, did not receive a timely response from an upstream server. Since the OpenWeatherMap API directly handles requests, this code was not received.
   - **Example:** Exceeding timeout waiting for a response from the OpenWeatherMap server.

6. **505 HTTP Version Not Supported**
   - **Description:** This code indicates that the server does not support the HTTP protocol version used. OpenWeatherMap API supports all standard HTTP versions, so this status code was not received.
   - **Example:** Attempting to use an incompatible HTTP version when sending a request to the API.

## Explanation of Unavailability of Some Status Codes

Some status codes may be unavailable in the context of the OpenWeatherMap API due to the following reasons:

- **Low probability of server errors:** OpenWeatherMap ensures high reliability and stability of its service, reducing the likelihood of receiving a "500 Internal Server Error".
- **Direct request handling:** The OpenWeatherMap API directly processes requests without intermediate gateways or proxies, which eliminates the possibility of receiving "502 Bad Gateway" and "504 Gateway Timeout" statuses.
- **High service availability:** The OpenWeatherMap service rarely enters "503 Service Unavailable" state due to technical maintenance or server overload.

## Tools

For API testing, you can also use Postman.

### Postman Request Examples

1. **Correct request**:
   - Method: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_CORRECT_API_KEY`
   - Expected status code: 200 OK

2. **Incorrect API key**:
   - Method: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?q=London&appid=incorrect_api_key`
   - Expected status code: 401 Unauthorized

3. **Absence of city name**:
   - Method: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?appid=YOUR_CORRECT_API_KEY`
   - Expected status code: 400 Bad Request

4. **Incorrect city name**:
   - Method: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?q=IncorrectCity&appid=YOUR_CORRECT_API_KEY`
   - Expected status code: 404 Not Found

5. **Exceeding request limit**:
   - Method: GET
   - URL: Send multiple requests in a short period (more than 60 per minute) to receive status code 429 Too Many Requests.

# RU


## Описание

Этот проект демонстрирует использование FastAPI для взаимодействия с OpenWeatherMap API и получения различных статус-кодов ответов. Мы используем различные тестовые случаи для исследования возможных статус-кодов и объясняем, почему некоторые из них невозможно получить.

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

    Этот эндпоинт возвращает статусы различных запросов к OpenWeatherMap API.


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
- Пустые параметры
- Недопустимое значение параметра `units`
- Широта вне допустимого диапазона
- Долгота вне допустимого диапазона
- Недопустимое значение параметра `cnt`
- Название города из пробела
- Длинное несуществующее название города
- Недопустимое значение параметра `lang`

### Полученные статус-коды , которые можно получить, имея бесплатную подписку на OpenWeatherMap

1. **200 OK**
   - Описание: Запрос был успешным, и сервер вернул ожидаемый результат.
   - Пример: Корректный API ключ и название города.

2. **401 Unauthorized**
   - Описание: Запрос требует аутентификации. Это обычно означает, что API ключ отсутствует или некорректен.
   - Пример: Некорректный API ключ или отсутствие API ключа.

3. **404 Not Found**
   - Описание: Запрашиваемый ресурс не найден. Это может означать, что указанный город не существует.
   - Пример: Некорректное имя города.

4. **400 Bad Request**
   - Описание: Сервер не может обработать запрос из-за ошибки клиента, например, недопустимое значение параметра.
   - Пример: Неверные координаты, недопустимые значения параметров (`units`, `cnt` и т.д.).

5. **429 Too Many Requests**
   - Описание: Превышено допустимое количество запросов. Этот статус-код может быть получен, если отправлено слишком много запросов за короткий период.
   - Пример: Превышение лимита запросов API (60 в минуту).

# Статус-коды, которые не были получены

1. **500 Internal Server Error**
   - **Описание:** Этот статус-код указывает на общую ошибку на сервере. В контексте OpenWeatherMap API, серверные ошибки редки и не были получены в ходе тестирования.

2. **501 Not Implemented**
   - **Описание:** Этот код указывает на то, что сервер не поддерживает функциональность, необходимую для выполнения запроса. В API OpenWeatherMap все поддерживаемые запросы были выполнены успешно, и этот статус-код не был получен.
   - **Пример:** Запрос, требующий функциональности, которая не реализована в API.

3. **502 Bad Gateway**
   - **Описание:** Этот статус-код указывает на то, что сервер, выступающий в роли шлюза или прокси, получил недействительный ответ от вышестоящего сервера. Так как OpenWeatherMap API напрямую обслуживает запросы, этот код не был получен.
   - **Пример:** Прокси-сервер не может получить корректный ответ от сервера OpenWeatherMap.

4. **503 Service Unavailable**
   - **Описание:** Этот код указывает на временную недоступность сервиса. OpenWeatherMap API обладает высокой доступностью, и во время тестирования сервис был доступен, поэтому данный статус-код не был получен.
   - **Пример:** Попытка доступа к API во время его технического обслуживания.

5. **504 Gateway Timeout**
   - **Описание:** Этот статус-код указывает на то, что сервер, выступающий в роли шлюза или прокси, не получил своевременный ответ от вышестоящего сервера. Так как OpenWeatherMap API напрямую обслуживает запросы, этот код не был получен.
   - **Пример:** Превышение времени ожидания ответа от сервера OpenWeatherMap.

6. **505 HTTP Version Not Supported**
   - **Описание:** Этот код указывает на то, что сервер не поддерживает используемую версию HTTP протокола. OpenWeatherMap API поддерживает все стандартные версии HTTP, поэтому данный статус-код не был получен.
   - **Пример:** Попытка использования несовместимой версии HTTP при отправке запроса к API.

## Объяснение невозможности получения некоторых статус-кодов

Некоторые статус-коды могут быть недоступны в контексте OpenWeatherMap API по следующим причинам:

- **Низкая вероятность серверных ошибок:** OpenWeatherMap обеспечивает высокую надежность и стабильность своего сервиса, что снижает возможность получения статуса "500 Internal Server Error".
- **Прямое обслуживание запросов:** API OpenWeatherMap напрямую обрабатывает запросы без промежуточных шлюзов или прокси, что исключает возможность получения статусов "502 Bad Gateway" и "504 Gateway Timeout".
- **Высокая доступность сервиса:** Сервис OpenWeatherMap редко находится в состоянии "503 Service Unavailable" из-за технических работ или перегрузок серверов.

   

## Инструменты

Для тестирования API вы также можете использовать Postman.

### Примеры запросов в Postman

1. **Корректный запрос**:
   - Метод: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_CORRECT_API_KEY`
   - Ожидаемый статус-код: 200 OK

2. **Некорректный API ключ**:
   - Метод: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?q=London&appid=incorrect_api_key`
   - Ожидаемый статус-код: 401 Unauthorized

3. **Отсутствие имени города**:
   - Метод: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?appid=YOUR_CORRECT_API_KEY`
   - Ожидаемый статус-код: 400 Bad Request

4. **Некорректное имя города**:
   - Метод: GET
   - URL: `https://api.openweathermap.org/data/2.5/weather?q=IncorrectCity&appid=YOUR_CORRECT_API_KEY`
   - Ожидаемый статус-код: 404 Not Found

5. **Превышение лимита запросов**:
   - Метод: GET
   - URL: Отправляйте множество запросов за короткий период (больше 60 в минуту), чтобы получить статус-код 429 Too Many Requests.

