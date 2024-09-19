import os
import subprocess

def optimize_font(input_path, output_path, glyphs, features, flavor):
    command = [
        'pyftsubset',
        input_path,
        f'--output-file={output_path}',
        f'--text={glyphs}',
        f'--flavor={flavor}',
        f'--layout-features={",".join(features)}',
        '--retain-gids',
        '--glyph-names',
        '--no-hinting'
    ]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        if os.path.exists(output_path):
            print(f"Font successfully saved to {output_path}")
        else:
            print("Error: file was not created.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing pyftsubset: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def get_input(prompt, default=None):
    value = input(f"{prompt} [{default}]: ") if default else input(f"{prompt}: ")
    return value if value else default

def main():
    print("Font Optimization Program")

    while True:
        input_path = get_input("Enter the full path to the source font")
        if os.path.exists(input_path):
            break
        print("Error: The specified file does not exist. Please check the path and try again.")

    output_dir = get_input("Enter the directory to save the optimized font", os.path.dirname(input_path))
    output_name = get_input("Enter the name for the optimized font", "optimized_font.woff2")
    output_path = os.path.join(output_dir, output_name)

    default_glyphs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{};:'\",./?<>|\\`~ "
    glyphs = get_input("Enter characters to keep (empty for default)", default_glyphs)

    default_features = ["cv11", "cv02", "cv03", "cv04"]
    features_input = get_input("Enter layout features separated by commas (empty for default)", ",".join(default_features))
    features = features_input.split(",") if features_input else default_features

    flavor = get_input("Enter font format (e.g., woff2)", "woff2")

    print("\nPlease review the entered data:")
    print(f"Source font: {input_path}")
    print(f"Optimized font will be saved as: {output_path}")
    print(f"Characters to keep: {glyphs}")
    print(f"Layout features: {features}")
    print(f"Font format: {flavor}")

    confirm = input("\nIs everything correct? (yes/no): ").lower()
    if confirm == 'yes':
        optimize_font(input_path, output_path, glyphs, features, flavor)
    else:
        print("Operation cancelled. Run the script again to enter new data.")

if __name__ == "__main__":
    main()