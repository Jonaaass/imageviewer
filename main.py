from setting import *
from taskbar import Taskbar


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Viewer")
        self.root.geometry(WINDOW_SIZE)
        self.root.iconbitmap("logo.ico")

        self.display_label = Label(self.root, bg="black")
        self.display_label.pack(fill=BOTH, expand=True)


        self.taskbar = Taskbar()
        self.taskbar.create_taskbar(self.root, self.display_label) 


if __name__ == "__main__":
    app = App()
    app.root.mainloop()