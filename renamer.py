import os
from tkinter import filedialog

chosen = filedialog.askdirectory()
os.chdir(chosen)

for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)
    new_name = '{}-{}{}'.format('22-02-07', file_name, file_ext)
    os.rename(file, new_name)

