from abc import ABC, abstractmethod
from tkinter import *
from tkinter import filedialog


class App:

    shape_path = ""
    image_path = ""

    def __init__(self, delegate):
        self.delegate = delegate

        self.app = Tk()

        self._shape_label = Label(self.app)
        self._image_label = Label(self.app)

        Button(self.app, text="Choose Shapefile", width=30, command=self.set_shape_path).pack()
        self._shape_label.pack()
        Button(self.app, text="Choose Image", width=30, command=self.set_image_path).pack()
        self._image_label.pack()
        Button(self.app, text="Plot!", width=30, command=self.plot).pack()

        self.app.mainloop()

    def set_shape_path(self):
        file = filedialog.askopenfile()
        self.shape_path = file.name
        self._shape_label.__setattr__("text", self.shape_path)
        self._shape_label.pack()

    def set_image_path(self):
        file = filedialog.askopenfile()
        self.image_path = file.name
        self._image_label.__setattr__("text", self.image_path)
        self._image_label.pack()

    def plot(self):
        self.delegate.get_shape_path(self.shape_path)
        self.delegate.get_image_path(self.image_path)
        self.app.quit()


class AppDelegate(ABC):

    @abstractmethod
    def get_shape_path(self, file_path):
        pass

    @abstractmethod
    def get_image_path(self, file_path):
        pass
