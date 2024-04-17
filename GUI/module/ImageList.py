import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import os
import shutil

class imageList(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.listbox = tk.Listbox(self, selectmode=tk.SINGLE)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.show_images()

    def delete_selected_image(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_image = self.listbox.get(selected_index)
            filename = os.path.join("images-test", selected_image)
            os.remove(filename)
            self.listbox.delete(selected_index)

    def get_selected_image(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            return self.listbox.get(selected_index)

    def add_image(self, filename):
        os.makedirs("images-test`", exist_ok=True)
        shutil.copy(filename, "images-test")
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
                old_path = os.path.join("images-test", old_filename)
                new_path = os.path.join("images-test", new_filename)
                os.rename(old_path, new_path)

    def show_images(self):
        image_folder = "images-test"
        if os.path.exists(image_folder):
            image_files = os.listdir(image_folder)
            for filename in image_files:
                if filename.endswith((".jpg", ".jpeg", ".png")):
                    self.listbox.insert(tk.END, filename)
