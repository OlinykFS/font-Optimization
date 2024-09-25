import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
import shutil

def find_pyftsubset():
    pyftsubset_path = shutil.which('pyftsubset')
    if pyftsubset_path:
        return pyftsubset_path
    else:
        messagebox.showerror("Error", "pyftsubset utility not found in the system PATH. Make sure it is installed correctly.")
        return None

def optimize_font(input_path, output_path, glyphs, features, flavor):
    pyftsubset_path = find_pyftsubset()
    if pyftsubset_path is None:
        return

    if not os.path.isfile(input_path):
        messagebox.showerror("Error", f"The specified input file does not exist:\n{input_path}")
        return

    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        try:
            os.makedirs(output_dir)
        except OSError as e:
            messagebox.showerror("Error", f"Failed to create the output directory:\n{output_dir}")
            return

    command = [
        pyftsubset_path,
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
        if os.path.exists(output_path):
            messagebox.showinfo("Success", f"Font successfully saved to:\n{output_path}")
        else:
            messagebox.showerror("Error", "Error: file was not created.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while executing pyftsubset:\n{e.stderr.strip()}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

class FontOptimizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Font Optimization Tool")
        self.master.geometry("600x500")

        # Используем тему для красивого интерфейса
        self.master.set_theme("arc")

        # Frame для ввода и вывода данных
        frame = ttk.Frame(self.master, padding="10 10 20 20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Input Font
        self.input_label = ttk.Label(frame, text="Source Font (.ttf, .otf, .woff, .woff2):", style="TLabel")
        self.input_label.grid(row=0, column=0, pady=5, sticky=tk.W)
        self.input_entry = ttk.Entry(frame, width=50)
        self.input_entry.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.input_button = ttk.Button(frame, text="Browse", command=self.browse_input)
        self.input_button.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Output Directory
        self.output_label = ttk.Label(frame, text="Output Directory:", style="TLabel")
        self.output_label.grid(row=2, column=0, pady=5, sticky=tk.W)
        self.output_entry = ttk.Entry(frame, width=50)
        self.output_entry.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        self.output_button = ttk.Button(frame, text="Browse", command=self.browse_output)
        self.output_button.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Output File Name
        self.output_name_label = ttk.Label(frame, text="Optimized Font Name:", style="TLabel")
        self.output_name_label.grid(row=4, column=0, pady=5, sticky=tk.W)
        self.output_name_entry = ttk.Entry(frame, width=50)
        self.output_name_entry.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
        self.output_name_entry.insert(0, "optimized_font")

        # Glyphs
        self.glyphs_label = ttk.Label(frame, text="Characters to keep:", style="TLabel")
        self.glyphs_label.grid(row=6, column=0, pady=5, sticky=tk.W)
        self.glyphs_entry = ttk.Entry(frame, width=50)
        self.glyphs_entry.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
        self.glyphs_entry.insert(0, "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

        # Features
        self.features_label = ttk.Label(frame, text="Layout Features (comma-separated):", style="TLabel")
        self.features_label.grid(row=8, column=0, pady=5, sticky=tk.W)
        self.features_entry = ttk.Entry(frame, width=50)
        self.features_entry.grid(row=9, column=0, padx=10, pady=5, sticky=tk.W)
        self.features_entry.insert(0, "cv11,cv02,cv03,cv04")

        # Flavor
        self.flavor_label = ttk.Label(frame, text="Font Format (default: woff2):", style="TLabel")
        self.flavor_label.grid(row=10, column=0, pady=5, sticky=tk.W)
        self.flavor_entry = ttk.Entry(frame, width=50)
        self.flavor_entry.grid(row=11, column=0, padx=10, pady=5, sticky=tk.W)
        self.flavor_entry.insert(0, "woff2")

        # Optimize Button
        self.optimize_button = ttk.Button(frame, text="Optimize Font", command=self.optimize)
        self.optimize_button.grid(row=12, column=0, padx=10, pady=20, sticky=tk.W)

    def browse_input(self):
        file_path = filedialog.askopenfilename(title="Select the source font file", filetypes=[("Font Files", "*.ttf;*.otf;*.woff;*.woff2")])
        if file_path:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def browse_output(self):
        dir_path = filedialog.askdirectory(title="Select output directory")
        if dir_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, dir_path)

    def optimize(self):
        input_path = self.input_entry.get()
        output_dir = self.output_entry.get()
        output_name = self.output_name_entry.get()
        glyphs = self.glyphs_entry.get()
        features = self.features_entry.get().split(",") if self.features_entry.get() else []
        flavor = self.flavor_entry.get()

        if not input_path or not output_dir or not output_name:
            messagebox.showwarning("Warning", "Please select source font and output directory, and provide a name for the optimized font.")
            return

        output_path = os.path.normpath(os.path.join(output_dir, f"{output_name}.{flavor}"))

        if os.path.exists(output_path):
            if messagebox.askyesno("File exists", f"The file '{output_name}.{flavor}' already exists. Do you want to overwrite it?"):
                os.remove(output_path)
            else:
                return

        optimize_font(input_path, output_path, glyphs, features, flavor)

if __name__ == "__main__":
    root = ThemedTk(theme="arc")
    app = FontOptimizerApp(root)
    root.mainloop()
