# Hashbrown GUI - v0.0.1-dev

# Author: Viihna Leraine (reach me at viihna@voidfucker.com / viihna.78 (Signal) / Viihna-Lehraine (Github))

# Licensed under GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.html)

# You may use this code for any purpose EXCEPT for the creation of proprietary derivatives. I encourage you to improve on my code or to include it in other projects if you find it helpful! I only ask that you to credit me as the original author, and more importantly, show me what you did. I'm still a rookie programmer, and would love to look at and learn from any changes you make!

# This program comes with ABSOLUTELY NO WARRANTY OR GUARANTEE OF ANY KIND



import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os

# Calculate file hash
def calculate_file_hash(file_path, algorithm):
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"File '{file_path}' not found.")
        return None
    
    try:
        hash_func = getattr(hashlib, algorithm)
        hash_obj = hash_func()
    except AttributeError:
        messagebox.showerror("Error", f"Unsupported algorithm '{algorithm}'")
        return None
    
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
            return hash_obj.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while reading the file. {e}")
        return None
    
# Handle file selection
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Handle hash calculation
def calculate_hash():
    file_path = file_entry.get()
    algorithm = algo_var.get()
    if not file_path or not algorithm:
        messagebox.showerror("Error", "Please select a file and an algorithm.")
        return
    hash_value = calculate_file_hash(file_path, algorithm)
    if hash_value:
        result_label.config(text=f"The {algorithm} hash of the file is: {hash_value}")

# Create the main application window
root = tk.Tk()
root.title ("Hashbrown")

# Create and place the widgets
tk.Label(root, text="Select a file:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select algorithm:").grid(row=1, column=0, padx=10, pady=10)
algorithms = [
    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512', 'blake2b', 'blake2s'
]
algo_var = tk.StringVar(value=algorithms[0])
algo_menu = tk.OptionMenu(root, algo_var, *algorithms)
algo_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate Hash", command=calculate_hash).grid(row=2, column=0, padx=10, pady=10)

result_label = tk.Label(root, text="The hash will be displayed here.")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Run the main event loop
root.mainloop()