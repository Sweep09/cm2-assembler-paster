import tkinter as tk
import pyperclip

root = tk.Tk()
root.withdraw()

file_path = tk.filedialog.askopenfilename(title="Select assembler text file")
with open(file_path, 'r') as file:
    fix = file.read().replace('\r', '')
    pyperclip.copy(fix)
    print('copied to clipboard')
