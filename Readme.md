
# Font Optimization Tool

This Python-based GUI tool allows users to optimize font files by subsetting specific glyphs, retaining layout features, and outputting them in various formats such as `woff2`. The tool uses `fontTools` and `pyftsubset` to handle font subsetting and provides an intuitive interface built with `tkinter`.

## Features
- **Subset fonts**: Remove unused glyphs from font files to reduce file size.
- **Retain layout features**: Customize which OpenType features (like `cv11`, `cv02`, etc.) should be preserved.
- **Multiple input formats**: Supports `.ttf`, `.otf`, `.woff`, and `.woff2` font formats.
- **Multiple output formats**: Output optimized fonts in different formats, including `woff2`.

## Requirements
Before running the tool, make sure you have the following dependencies installed:

1. **Python 3.10+**
2. **Required Python packages**:
    - `fonttools`
    - `ttkthemes`
    - `pyinstaller` (for converting to `.exe`)
    - `brotli` (for WOFF2 font support)

Install the required packages using `pip`:

```bash
pip install fonttools ttkthemes brotli
```

Ensure `pyftsubset` is installed and accessible in your system's PATH:

```bash
pip install fonttools[subset]
```

## Usage

### Running the Application
You can run the tool directly using Python:

```bash
python main.py
```

### Converting to an Executable (.exe)

To distribute the application as a standalone executable, use **PyInstaller**:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed main.py
   ```

This will create an `.exe` file inside the `dist/` folder that can be run on any Windows machine.

## Interface Overview

- **Source Font**: Select the source font file (`.ttf`, `.otf`, `.woff`, or `.woff2`).
- **Output Directory**: Choose where the optimized font will be saved.
- **Optimized Font Name**: Enter a name for the new, optimized font (without extension).
- **Characters to Keep**: Enter the glyphs (characters) you want to retain.
- **Layout Features**: Specify which OpenType features should be retained in the output font.
- **Font Format**: Select the output format (default is `woff2`).

## License

This project is licensed under the MIT License.

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request.
