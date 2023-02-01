from tkinter import *
from tkinter import filedialog
from functools import *
import sys
from models.paths import PathModel
from tools.apptests import AppTests
from models.empyriondb import DataBaseModel


class DropMenuFiles(Menu):
    __observers = []
    def __init__(self, parent):
        Menu.__init__(self, parent)

        self.parent = parent
        self.path_model = PathModel()
        self.app_test = AppTests()
        self.empyriondb_model = DataBaseModel()
        self.fileMenu = Menu(self, tearoff=FALSE)
        self.add_cascade(label="Fichier",underline=0, menu=self.fileMenu)
        self.openmenu = Menu(self, tearoff=FALSE)
        self.fileMenu.add_command(label="Ouvrir", underline=1, command=self.open_file)
        self.fileMenu.add_cascade(label="Récent", menu=self.openmenu)

        paths = self.path_model.get_all_paths()

        if paths:
            for i,  row in enumerate(paths):
                self.openmenu.add_command(label= row[0], command=partial(self.open_last_file,i))

        self.fileMenu.add_command(label="Quitter", underline=1, command=self.quit)

    """ close the app """
    def quit(self):
        sys.exit(0)


    """ open_file is the manual opening file function"""
    def open_file(self):
        db_path = filedialog.askopenfilename(initialdir = "/",title = "Selectionner un fichier",filetypes = ((" Fichier Database","*.db"),("Tous","*.*")))
        is_sqlite3 = False
        is_empyrion_file = False

        if db_path:
            is_sqlite3 = self.app_test.is_SQLite3(db_path)
            if is_sqlite3:
                is_empyrion_file = self.empyriondb_model.is_empyrion_db(db_path)

        if db_path and is_sqlite3 and is_empyrion_file:
            self.path_model.add_in_config_db(db_path) # add new path in config db if only is real new
            self.notify_observers(db_path)
            if self.path_model.is_in_db(db_path): # if the path do not exist in the config db then 
                self.openmenu.add_command(label= db_path, command=partial(self.open_last_file)) # add new path to the recent list paths


    """ open_last_file is triggered when a recorded path is selected """
    def open_last_file(self,i):
        db_path = self.openmenu.entrycget(i, "label")
        self.notify_observers(db_path)

    def add_observers(self, observers):
        for observer in observers:
            self.__observers.append(observer)
    

    def notify_observers(self, db_path):
        for observer in self.__observers:
            observer.update_db(db_path)