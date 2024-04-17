import tkinter as tk
from datetime import datetime
from tkinter import ttk, simpledialog, messagebox, filedialog

from PIL import Image, ImageTk
import os

from Artemida.GUI.module.ImageAnalyzer import analyze_image
from Artemida.GUI.module.ImageList import imageList


class ArtemidaApp:
    def __init__(self, master):
        self.master = master
        master.title("Artemida v0.1")
        master.geometry("900x900")
        master.resizable(False, False)
        master.iconbitmap("index.ico")
        self.create_menu()
        self.create_image_list()
        self.create_buttons()
        self.create_image_preview()
    '''master.configure(bg="gray")'''


    def create_menu(self):
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Загрузить изображение", command=self.load_image)
        self.file_menu.add_command(label="Изменить название", command=self.rename_image)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)

    def create_image_list(self):
        self.image_list = imageList(self.master)
        self.image_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    def create_buttons(self):
        button_frame = tk.Frame(self.master)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.delete_button = ttk.Button(button_frame, text="Удалить", command=self.delete_image)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.exit_button = ttk.Button(button_frame, text="Выход", command=self.exit_program)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.analyze_button = ttk.Button(button_frame, text="Анализировать", command=self.analyze_images)
        self.analyze_button.pack(side=tk.LEFT, padx=10, pady=10)

    def create_image_preview(self):
        self.image_preview_label = tk.Label(self.master, text="Предпросмотр", anchor=tk.W)
        self.image_preview_label.pack(fill=tk.X, padx=10, pady=(10, 0), side=tk.TOP)
        self.image_list.listbox.bind("<ButtonRelease-1>", self.show_preview)

    def exit_program(self):
        self.master.destroy()

    def delete_image(self):
        self.image_list.delete_selected_image()
        self.hide_preview(None)

    def analyze_images(self):
        selected_image = self.image_list.get_selected_image()
        if selected_image:
            analyze_image(selected_image)

    def load_image(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.image_list.add_image(filename)

    def rename_image(self):
        self.image_list.rename_selected_image()

    def show_preview(self, event):
        selected_index = self.image_list.listbox.curselection()
        if selected_index:
            selected_image = self.image_list.listbox.get(selected_index)
            image_path = os.path.join("images-test", selected_image)
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_preview_label.config(image=photo)
            self.image_preview_label.image = photo


    def hide_preview(self, event):
        self.image_preview_label.config(image=None)
        self.image_preview_label.image = None

root = tk.Tk()
app = ArtemidaApp(root)
root.mainloop()
