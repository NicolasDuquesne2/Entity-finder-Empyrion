from tkinter import *
from functools import *
from models.paths import PathModel
from views.dropmenufiles import DropMenuFiles
from views.mainbrowserframe import MainBrowserFrame
from tools.databases import Database

class Mainwindow(Tk):
    __observers = []
    def __init__(self):
        Tk.__init__(self)
        self.database = Database()
        self.path_model = PathModel()
        self.dropMenu = DropMenuFiles(self)
        self.config(menu=self.dropMenu)
        self.main_browser_frame = MainBrowserFrame(self)

        self.dropMenu.add_observers([self])
        
        self.add_observers([
            self.main_browser_frame.main_data_frame.main_display_frame.list_box_frame.list_box,
            self.main_browser_frame.main_data_frame.main_display_frame.tree_view_frame.tree_view
        ])

        self.path_model.check_paths()
        self.path_model.set_last_db_path(self.database)
    
    def add_observers(self, observers):
        for observer in observers:
            self.__observers.append(observer)
    
    def notify_observers(self, database):
        for observer in self.__observers:
            observer.update_db(database)

    def update_db(self, db_name):
        self.database.open(db_name)
        self.notify_observers(self.database)