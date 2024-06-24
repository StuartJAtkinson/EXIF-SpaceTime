# EXIF-SpaceTime
An application focused on editing geolocation & time metadata

## Handling Metadata/EXIF Data

This guide will help you understand how to handle metadata/EXIF data using suitable libraries. We will cover the following steps:

1. Loading Metadata
2. Extracting Metadata
3. Exporting Metadata
4. Comparing Metadata
5. Writing Metadata

### Suitable Libraries

- **ExifTool**: A powerful command-line application for reading, writing, and editing meta information in a wide variety of files.
- **Pillow (PIL)**: A Python Imaging Library that adds image processing capabilities to your Python interpreter.
- **piexif**: A Python library to simplify the process of inserting and modifying EXIF data.
- **exifread**: A Python library to extract EXIF metadata from images.

### 1. Loading Metadata

#### Using ExifTool

```python
import subprocess

def load_metadata(file_path):
    result = subprocess.run(['exiftool', file_path], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

metadata = load_metadata('example.jpg')
print(metadata)
```

#### Using Pillow

```python
from PIL import Image

def load_metadata(file_path):
    image = Image.open(file_path)
    return image._getexif()

metadata = load_metadata('example.jpg')
print(metadata)
```

### 2. Extracting Metadata

#### Using piexif

```python
import piexif

def extract_metadata(file_path):
    exif_dict = piexif.load(file_path)
    return exif_dict

metadata = extract_metadata('example.jpg')
print(metadata)
```

#### Using exifread

```python
import exifread

def extract_metadata(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
    return tags

metadata = extract_metadata('example.jpg')
print(metadata)
```

### 3. Exporting Metadata

#### Using ExifTool

```python
import subprocess

def export_metadata(file_path, output_file):
    subprocess.run(['exiftool', '-json', file_path, '-o', output_file])

export_metadata('example.jpg', 'metadata.json')
```

### 4. Comparing Metadata

#### Using Python Dictionaries

```python
def compare_metadata(metadata1, metadata2):
    differences = {}
    for key in metadata1.keys():
        if key in metadata2 and metadata1[key] != metadata2[key]:
            differences[key] = (metadata1[key], metadata2[key])
    return differences

metadata1 = extract_metadata('example1.jpg')
metadata2 = extract_metadata('example2.jpg')
differences = compare_metadata(metadata1, metadata2)
print(differences)
```

### 5. Writing Metadata

#### Using piexif

```python
import piexif

def write_metadata(file_path, metadata):
    exif_bytes = piexif.dump(metadata)
    piexif.insert(exif_bytes, file_path)

metadata = extract_metadata('example.jpg')
metadata['0th'][piexif.ImageIFD.Make] = "New Camera Make"
write_metadata('example.jpg', metadata)
```

#### Using ExifTool

```python
import subprocess

def write_metadata(file_path, tag, value):
    subprocess.run(['exiftool', f'-{tag}={value}', file_path])

write_metadata('example.jpg', 'Make', 'New Camera Make')
```

By following this guide, you should be able to handle metadata/EXIF data effectively using various libraries and tools. Each step provides example code snippets to help you get started quickly.