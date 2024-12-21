import tkinter as tk
from tkinter import filedialog
import pyperclip

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title="Select assembler text file")
with open(file_path, 'r', encoding="UTF-8") as file:
    fix = file.read().replace('\r', '')
    pyperclip.copy(fix)
    print('copied to clipboard')
