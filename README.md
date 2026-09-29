# Organized

A Python CLI tool for automatically organizing files into folders based on their names.
*I was bored


 **Warning:** Organized moves files and creates directories automatically. Test it on a copy of your files before using it on important data.

## Features

* Groups files based on common parts of their names
* Creates a separate folder for individual files
* Organizes TV show episodes into season folders
* Supports the current directory
* Supports a custom directory
* Can be built as a standalone executable with PyInstaller

## Example

Given files like:

```text
The.Movie.S02E01.720p.mkv
The.Movie.S02E02.720p.mkv
The.Movie.S03E01.720p.mkv
```

The program can organize them into:

```text
The.Movie/
├── Season 2/
│   ├── The.Movie.S02E01.720p.mkv
│   └── The.Movie.S02E02.720p.mkv
└── Season 3/
    └── The.Movie.S03E01.720p.mkv
```

## Requirements

* Python 3.10+
* PyInstaller (only required for building the executable)

## Run from source

Clone the repository:

```bash
git clone <repository-url>
cd organized
```

Run:

```bash
python src/main.py
```

## Build

Install PyInstaller:

```bash
pip install pyinstaller
```

Build a standalone executable:

```bash
pyinstaller --onefile --name organized src/main.py
```

The executable will be created in:

```text
dist/organized
```

Python does not need to be installed on the target system to run the generated executable.

## Project Structure

```text
organized/
├── src/
│   ├── main.py
│   ├── known_dir.py
│   ├── custom_dir.py
│   └── make_subdir.py
├── .gitignore
├── README.md
└── LICENSE
```

## Status

This project is currently under development.

## License

This project is licensed under the MIT License.
