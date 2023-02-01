from tkinter import PanedWindow
from views.maindataframe import MainDataFrame
from tools.configs import ConfigsParams


class MainBrowserFrame(PanedWindow):

    def __init__(self, parent):
        self.config_main_browser_panedwindow = ConfigsParams().config_main_browser_panedwindow

        PanedWindow.__init__(self, parent, orient= self.config_main_browser_panedwindow['orient'], 
                            height=self.config_main_browser_panedwindow['height'],
                            width=self.config_main_browser_panedwindow['width'])
        
        self.pack(side=self.config_main_browser_panedwindow['side'], 
                  expand=self.config_main_browser_panedwindow['expand'], 
                  fill=self.config_main_browser_panedwindow['fill'], 
                  pady=self.config_main_browser_panedwindow['pady'], 
                  padx=self.config_main_browser_panedwindow['padx'])


        self.main_data_frame = MainDataFrame(self)


