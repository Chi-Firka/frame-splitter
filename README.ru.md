# Frame Splitter

Инструмент для преобразования анимированных PNG, GIF файлов в атласные карты.

## Описание

Этот скрипт позволяет:
- Извлекать отдельные кадры из анимированных PNG файлов
- Создавать горизонтальные атласные карты из кадров анимации
- Обрабатывать как отдельные файлы, так и целые директории с PNG файлами
- Сохранять пропорции и размеры исходных кадров в атласной карте

## Требования

- Python 3.x
- Pillow 10.2.0

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Chi-Firka/frame-splitter.git
cd frame-splitter
```

2. Установите зависимость одним из способов:
```bash
pip install Pillow==10.2.0
# или
pip install -r requirements.txt
```

## Использование

### Обработка одного файла

```bash
python frame-splitter.py "path/to/file.png(.gif)"
```

### Обработка директории

```bash
python frame-splitter.py "path/to/directory"
```

### Результаты

- При обработке одного файла: создается новый файл с суффиксом `_atlas.png` в той же директории
- При обработке директории: создается поддиректория `atlas_output`, сохраняя структуру исходной директории

## Особенности

- Поддерживаются кадры любого размера
- Выходная атласная карта сохраняет высоту исходных кадров
- Ширина атласной карты равна (количество кадров × ширина кадра)
- Поддерживается прозрачность (формат RGBA)
- Автоматическое создание необходимых директорий для выходных файлов

## Примеры

## Лицензия

MIT License

Copyright (c) 2025 Chi-Firka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.