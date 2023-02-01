from tkinter.ttk import Combobox
from tools.configs import ConfigsParams
from models.entity import EntityModel

class ComboBox(Combobox):

    __observers = []
    def __init__(self, parent, datas):

        Combobox.__init__(self, parent, values=datas)
        self.bind("<<ComboboxSelected>>", self.handle_selection)

    def handle_selection(self, event=None):
        selected = self.get()
        print(selected)
        self.notify_observers(selected)


    def add_observer(self, observer):
        self.__observers.append(observer)


    def notify_observers(self, text):

        for observer in self.__observers:
            observer.update(text)