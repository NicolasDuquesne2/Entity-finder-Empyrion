from tkinter import Listbox, END
from tools.configs import ConfigsParams
from models.entity import EntityModel
from tools.apptests import AppTests

class DataListBox(Listbox):
    __observers = []

    def __init__(self, parent):
        self.configs = ConfigsParams()
        Listbox.__init__(self, parent, width=self.configs.config_listbox['width'])
        self.parent = parent
        self.database = None
        self.entity_model = EntityModel()
        self.app_tests = AppTests()
        self.bind("<<ListboxSelect>>", self.select_item)

    def select_item(self, event=None):
        index = self.curselection()
        if index:
            text = self.get(index)
            text_for_sql = self.app_tests.handle_quotes(text)
            self.notify_observers(text_for_sql)
    
    def populate(self, rows):
        if rows:
            for row in rows:
                if row[0]:
                    self.insert(END, row[0])

    def dispopulate(self):
        self.delete(0, self.size()-1)

    def update(self, text):
        self.dispopulate()
        rows =  self.database.select(self.entity_model.get_one_db_entity_type_sql(text), self.database.name)
        if rows:
            self.populate(rows)
    
    def update_db(self, database):
        self.database = database
        self.dispopulate()
        rows =  self.database.select(self.entity_model.db_query_distinct_entity, self.database.name)
        if rows:
            self.populate(rows)

    
    def add_observer(self, observer):
        self.__observers.append(observer)


    def notify_observers(self, text):

        for observer in self.__observers:
            observer.update(text)