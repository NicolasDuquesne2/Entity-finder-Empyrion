from tkinter import Entry, StringVar, ttk
from tools.configs import ConfigsParams


class SearchBar(Entry):
    def __init__(self, parent):
        self.parent = parent
        self.configs_params = ConfigsParams().config_search_bar
        self.string_var = StringVar()
        

    
    def search(self, *args):
       pass

class MainSearchBar(SearchBar):
    def __init__(self, parent):
        SearchBar.__init__(self, parent)
        self.string_var.trace("w", self.search) 
        Entry.__init__(self, parent, width=self.configs_params['width'], textvariable=self.string_var)
        ttk.Style().configure("TEntry", padding=6, relief='flat', foreground="black")
    
    def search(self, *args):
        word = self.string_var.get()
        print(word)


class ListBoxSearchBar(SearchBar):

    __observers = []
    def __init__(self, parent):
        SearchBar.__init__(self, parent)
        self.string_var.trace("w", self.handle_stringvar_trace) 
        Entry.__init__(self, parent, width=self.configs_params['width'], textvariable=self.string_var)
        ttk.Style().configure("TEntry", padding=6, relief='flat', foreground="black")
    

    def add_observer(self, observer):
        self.__observers.append(observer)


    def notify_observers(self, text):
        for observer in self.__observers:
            observer.update(text)

    def handle_stringvar_trace(self, *args):
        word = self.string_var.get()
        word_for_sql = ConfigsParams().handle_quotes(word)
        self.notify_observers(word_for_sql)
