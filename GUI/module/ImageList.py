import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
import os

class imageList(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

    def delete_selected_image(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_image = self.listbox.get(selected_index)
            filename = os.path.join("../../images-test", selected_image)
            os.remove(filename)
            self.listbox.delete(selected_index)

    def get_selected_image(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            return self.listbox.get(selected_index)

    def add_image(self, filename):
        os.makedirs("../../images-test", exist_ok=True)
        os.replace(filename, os.path.join("../../images-test", os.path.basename(filename)))
        self.listbox.insert(tk.END, os.path.basename(filename))

    def rename_selected_image(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            old_filename = self.listbox.get(selected_index)
            new_filename = simpledialog.askstring("Изменить название", "Введите новое название изображения:")
            if new_filename:
                if "." not in new_filename:
                    messagebox.showerror("Ошибка", "Введите название файла в формате 'имя.расширение'")
                    return
                self.listbox.delete(selected_index)
                self.listbox.insert(selected_index, new_filename)
                old_path = os.path.join("../../images-test", old_filename)
                new_path = os.path.join("../../images-test", new_filename)
                os.rename(old_path, new_path)
