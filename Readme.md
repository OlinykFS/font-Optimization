# Font Optimization Script

This Python script provides an interactive way to optimize fonts using the `pyftsubset` tool from the `fonttools` library. It allows users to customize various aspects of font subsetting, including which characters to keep, layout features to retain, and the output font format.

## Features

- Interactive command-line interface
- Customizable character set for subsetting
- Configurable layout features
- Flexible input and output paths
- Support for different font formats (e.g., woff2)
- Error handling and input validation

## Prerequisites

Before running this script, ensure you have Python installed on your system. You also need to install the `fonttools` library, which provides the `pyftsubset` command. You can install it using pip:

```
pip install fonttools
```

## Usage

1. Save the script as `optimize_font.py`.

2. Run the script:
   ```
   python optimize_font.py
   ```

3. Follow the prompts to enter:
   - Full path to the source font
   - Directory to save the optimized font
   - Name for the optimized font
   - Characters to keep (or press Enter for default)
   - Layout features to retain (or press Enter for default)
   - Output font format

4. Review the entered data and confirm to proceed with the optimization.

5. The script will process the font and save the optimized version to the specified output path.

## Example

```
Font Optimization Program
Enter the full path to the source font: C:\fonts\original.ttf
Enter the directory to save the optimized font [C:\fonts]: 
Enter the name for the optimized font [optimized_font.woff2]: custom_font.woff2
Enter characters to keep (empty for default): ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
Enter layout features separated by commas (empty for default): cv01,cv02
Enter font format (e.g., woff2) [woff2]: 

Please review the entered data:
Source font: C:\fonts\original.ttf
Optimized font will be saved as: C:\fonts\custom_font.woff2
Characters to keep: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789
Layout features: ['cv01', 'cv02']
Font format: woff2

Is everything correct? (yes/no): yes
```

## Customization

- **Character Set**: By default, the script includes uppercase and lowercase Latin letters, numbers, and common punctuation. You can customize this by entering your desired characters when prompted.
- **Layout Features**: The default features are `cv11`, `cv02`, `cv03`, and `cv04`. You can specify different features by entering them as a comma-separated list.
- **Font Format**: The default output format is `woff2`, but you can change this to other formats supported by `pyftsubset`.

## Notes

- This script uses the `pyftsubset` tool with the following additional flags:
  - `--retain-gids`: Keeps the original glyph indices
  - `--glyph-names`: Keeps the glyph names in the font
  - `--no-hinting`: Removes hinting information to reduce file size

## Error Handling

The script includes error handling for common issues such as:
- Non-existent input files
- Errors during the font optimization process
- Unexpected exceptions

If any errors occur, the script will display an appropriate error message and, in some cases, allow you to retry the input.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.
