# Artemida

Artemida - это программный проект для обнаружения и аннотации областей на изображениях горных рельефов с использованием методов компьютерного зрения.

## Установка

1. Клонируйте репозиторий с помощью следующей команды:
    ```
    git clone https://github.com/your_username/Artemida.git
    ```
2. Перейдите в каталог Artemida:
    ```
    cd Artemida
    ```
3. Установите зависимости, указанные в файле `requirements.txt`:
    ```
    pip install -r requirements.txt
    ```

## Использование

### Подготовка изображений

1. Поместите изображения для анализа в папку `images-test`.

### Запуск программы

1. Запустите файл `main.py` с помощью интерпретатора Python:
    ```
    python main.py
    ```

2. После запуска программы на экране появятся аннотированные изображения с выделенными областями горных рельефов.

## Описание файлов и модулей

- `main.py`: Основной файл программы, который содержит точку входа и основной код для обработки изображений.
- `Artemida/module/`: Директория с модулями, содержащими различные функции и классы для обработки изображений.
    - `preprocessing.py`: Модуль для предварительной обработки изображений перед анализом.
    - `depth_estimation.py`: Модуль для оценки глубины изображений горных рельефов.
    - `heatmap_visualization.py`: Модуль для визуализации карты глубины в виде тепловой карты.
    - `annatationVSLS.py`: Модуль для аннотации областей на изображении и добавления подписей.
