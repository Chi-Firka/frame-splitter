# Frame Splitter

A tool for converting animated PNG and GIF files into sprite atlases.

[Русская версия](README.ru.md)

## Description

This script allows you to:
- Extract individual frames from animated PNG/GIF files
- Create horizontal sprite atlases from animation frames
- Process both single files and entire directories with PNG/GIF files
- Preserve the proportions and dimensions of source frames

## Requirements

- Python 3.x
- Pillow 10.2.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Chi-Firka/frame-splitter.git
cd frame-splitter
```

2. Install the dependency using one of these methods:
```bash
pip install Pillow==10.2.0
# or
pip install -r requirements.txt
```

## Usage

### Processing a single file

```bash
python frame-splitter.py "path/to/file.png(.gif)"
```

### Processing a directory

```bash
python frame-splitter.py "path/to/directory"
```

### Results

- When processing a single file: creates a new file with the `_atlas.png` suffix in the same directory
- When processing a directory: creates an `atlas_output` subdirectory, preserving the source directory structure

## Features

- Supports frames of any size
- Output atlas preserves the height of source frames
- Atlas width equals (number of frames × frame width)
- Supports transparency (RGBA format)
- Automatic creation of necessary directories for output files

## Examples

## License

MIT License

Copyright (c) 2024 Chi-Firka

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