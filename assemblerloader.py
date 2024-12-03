import tkinter as tk
from tkinter import filedialog
import pyperclip 

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

processed_code: str = ""
with open(file_path, 'r') as file:
    processed_code = ''.join(line.strip() + '\n' for line in file)
    pyperclip.copy(processed_code)
    print('copied to clipboard')