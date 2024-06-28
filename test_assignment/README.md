# Image Duplicate Finder


# EN

## Description

Modsen Image Duplicate Finder is a tool for detecting duplicate images in specified directories. The program supports JPG, PNG, GIF, BMP, JPEG formats and uses hash sums for efficient duplicate detection.

### Installing Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/YuryHaurylenka/modsen.git
    cd modsen
    ```

2. Install the dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Project

1. Prepare the folders with the images you want to check for duplicates.
2. Specify the paths to these folders in the `main.py` script by editing the `folder1` and `folder2` variables.
3. Run the script:

    ```bash
    python main.py
    ```
   
### Duplicate visualization

![](https://github.com/YuryHaurylenka/modsen_python/blob/develop/test_assignment/screenshots/visualizing.png)

### Running the tests

1. Navigate to the assignment folder:
   
   ```bash
   cd test_assignment/
   ```

2. Run the tests using the pytest command:
   
   ```bash
   pytest
   ```
   

# RU

## Описание

Modsen Image Duplicate Finder — это инструмент для поиска дубликатов изображений в указанных директориях. Программа поддерживает форматы JPG, PNG, GIF, BMP, JPEG и использует хэш-суммы для эффективного обнаружения дубликатов.


### Установка зависимостей

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/YuryHaurylenka/modsen.git
    cd modsen
    ```

2. Установите зависимости, перечисленные в `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

### Запуск проекта

1. Подготовьте папки с изображениями, которые вы хотите проверить на наличие дубликатов.
2. Укажите пути к этим папкам в скрипте `main.py`, отредактировав переменные `folder1` и `folder2`.
3. Запустите скрипт:

    ```bash
    python main.py
    ```
   
### Визуализация дубликатов

![](https://github.com/YuryHaurylenka/modsen_python/blob/develop/test_assignment/screenshots/visualizing.png)
   
### Запуск тестов

1. Перейдите в папку с заданием:

   ```bash
   cd test_assignment/
   ```

2. Запустите тесты командой pytest:
   
   ```bash
   pytest
   ```
