from tkinter import PanedWindow
from tools.configs import ConfigsParams
from views.listbox import DataListBox
from views.searchbar import ListBoxSearchBar

class ListBoxFrame(PanedWindow):

    def __init__(self, parent):
        self.config_main_browser_panedwindow = ConfigsParams().config_listbox_panedwindow

        PanedWindow.__init__(self,parent, orient= self.config_main_browser_panedwindow['orient'], 
                            height=self.config_main_browser_panedwindow['height'],
                            width=self.config_main_browser_panedwindow['width'])
        

        self.pack(side=self.config_main_browser_panedwindow['side'], 
                  expand=self.config_main_browser_panedwindow['expand'], 
                  fill=self.config_main_browser_panedwindow['fill'], 
                  pady=self.config_main_browser_panedwindow['pady'], 
                  padx=self.config_main_browser_panedwindow['padx'])
        
        self.search_bar = ListBoxSearchBar(self)
        self.search_bar.pack(side="left")
        self.add(self.search_bar)
        self.list_box = DataListBox(self)
        self.add(self.list_box)
        self.search_bar.add_observer(self.list_box)
        

        
