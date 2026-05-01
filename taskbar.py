from setting import *



class Taskbar:
    def create_taskbar(self, root, display_label):
        self.current_image = None
        self._clipboard_image = None
        self.root = root
        self.display_label = display_label

        self.menubar = Menu(root)
        root.config(menu=self.menubar)

        file_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Öffnen",    command=self.open_file)
        file_menu.add_command(label="Speichern", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Beenden",   command=root.quit)

        edit_menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=edit_menu)

        edit_menu.add_command(label="Kopieren",  command=self.copy)
        edit_menu.add_command(label="Einfügen",  command=self.paste)

    def open_file(self):
        self.path = filedialog.askopenfilename(
            title="Datei öffnen",
            filetypes=[
                ("Pictures", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("all files", "*.*"),
            ]
        )
        if self.path:
            self.current_image = Image.open(self.path)
            w = self.root.winfo_width()
            h = self.root.winfo_height()
            self.current_image.thumbnail((w, h))
            self.photo = ImageTk.PhotoImage(self.current_image)
            self.display_label.config(image=self.photo)

    def save_file(self):
        path = filedialog.asksaveasfilename(
            title="Speichern unter",
            defaultextension=".png",
            filetypes=[
                ("PNG",       "*.png"),
                ("JPEG",      "*.jpg"),
                ("all files", "*.*"),
            ]
        )
        if path:
            print(f"gespeichert: {path}")

    def copy(self):
        if self.current_image is None:
            print("Kein Bild geöffnet")
            return

        buf = io.BytesIO()
        self.current_image.convert("RGB").save(buf, format="PNG")
        self._clipboard_image = self.current_image.copy()
        print("Bild kopiert")

    def paste(self):
        if self._clipboard_image is None:
            print("Zwischenablage ist leer")
            return

        self.current_image = self._clipboard_image.copy()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        self.current_image.thumbnail((w, h))
        self.photo = ImageTk.PhotoImage(self.current_image)
        self.display_label.config(image=self.photo)
        print("Bild eingefügt")