import tkinter as tk
from tkinter import filedialog, messagebox
import os

class GUIInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("File/Folder Information Viewer")
        self.create_menu()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Open Folder", command=self.open_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)
        
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.display_file_info(file_path)
        
    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.display_folder_info(folder_path)
        
    def display_file_info(self, file_path):
        file_info = os.stat(file_path)
        info_window = tk.Toplevel(self.root)
        info_window.title("File Information")
        
        info_text = tk.Text(info_window, wrap=tk.WORD)
        info_text.insert(tk.END, f"File: {file_path}\n")
        info_text.insert(tk.END, f"Size: {file_info.st_size} bytes\n")
        info_text.insert(tk.END, f"Created: {self.format_time(file_info.st_ctime)}\n")
        info_text.insert(tk.END, f"Modified: {self.format_time(file_info.st_mtime)}\n")
        info_text.pack(expand=True, fill=tk.BOTH)
        
    def display_folder_info(self, folder_path):
        folder_info = os.stat(folder_path)
        info_window = tk.Toplevel(self.root)
        info_window.title("Folder Information")
        
        info_text = tk.Text(info_window, wrap=tk.WORD)
        info_text.insert(tk.END, f"Folder: {folder_path}\n")
        info_text.insert(tk.END, f"Created: {self.format_time(folder_info.st_ctime)}\n")
        info_text.insert(tk.END, f"Modified: {self.format_time(folder_info.st_mtime)}\n")
        info_text.pack(expand=True, fill=tk.BOTH)
        
    def format_time(self, timestamp):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIInterface(root)
    root.mainloop()