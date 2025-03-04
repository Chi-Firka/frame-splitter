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

## Example
```py
py frame-splitter.py "E:\Desktop\sprite-splitter\av.gif"
```
From:
`av.gif (90x90)`

![av](https://github.com/user-attachments/assets/25d1fe0c-423d-4031-90b0-9990dcd96ebc)

To:
`av_atlas.png (720x90)`

![av_atlas](https://github.com/user-attachments/assets/6062c4bc-5577-44da-8605-8e75b5c342a1)



## License

MIT License

Read LICENCE.md for more details
