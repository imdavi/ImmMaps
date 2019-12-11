from abc import ABC, abstractmethod
from tkinter import *
from tkinter import filedialog

"""
The App class defines the behaviour of a GUI application to select the file paths.
"""

class App:

    shape_path = ""
    image_path = ""

    def __init__(self, delegate):
        # Sets the delegate object
        self.delegate = delegate
        # Creates the main window
        self.app = Tk(screenName="Select map data")
        # creates the labels
        self._shape_label = Label(self.app)
        self._image_label = Label(self.app)
        # Instantiates the button with its method and places it on the window
        Button(self.app, text="Choose Shapefile", width=30, command=self.set_shape_path).pack()
        # places the label
        self._shape_label.pack()
        # instantiates the second button
        Button(self.app, text="Choose Image", width=30, command=self.set_image_path).pack()
        # places the second label
        self._image_label.pack()
        # instantiates the last button
        Button(self.app, text="Plot!", width=30, command=self.plot).pack()
        # starts the app main loop
        self.app.mainloop()

    def set_shape_path(self):
        # uses a function dialog to select file 
        file = filedialog.askopenfile()
        # gets the file path
        self.shape_path = file.name
        # defines the label text
        self._shape_label.__setattr__("text", self.shape_path)
        self._shape_label.pack()

    def set_image_path(self):
        # uses a function dialog to select file 
        file = filedialog.askopenfile()
        # gets the file path
        self.image_path = file.name
        # defines the label text
        self._image_label.__setattr__("text", self.image_path)
        self._image_label.pack()

    # this method is called when the Plot button is pressed
    def plot(self):
        # sends the paths to the delegate
        self.delegate.get_shape_path(self.shape_path)
        self.delegate.get_image_path(self.image_path)
        # quits the application
        self.app.quit()

"""
This is an abstract class that defines the Delegate protocol of the GUI app.
Only determines the implementation of the two methods, both for obtaining the file paths.
"""
class AppDelegate(ABC):

    @abstractmethod
    def get_shape_path(self, file_path):
        pass

    @abstractmethod
    def get_image_path(self, file_path):
        pass
