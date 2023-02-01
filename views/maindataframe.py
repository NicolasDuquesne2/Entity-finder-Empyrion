from tkinter import PanedWindow
from tools.configs import ConfigsParams
from views.toolbar import ToolBar
from views.maindisplayframe import MainDisplayFrame

class MainDataFrame(PanedWindow):

    def __init__(self, parent):
        self.config_main_data_panedwindow = ConfigsParams().config_main_data_panedwindow

        PanedWindow.__init__(self, parent, orient= self.config_main_data_panedwindow['orient'], 
                            height=self.config_main_data_panedwindow['height'],
                            width=self.config_main_data_panedwindow['width'])
        
        self.pack(side=self.config_main_data_panedwindow['side'], 
                    expand=self.config_main_data_panedwindow['expand'], 
                    fill=self.config_main_data_panedwindow['fill'], 
                    pady=self.config_main_data_panedwindow['pady'], 
                    padx=self.config_main_data_panedwindow['padx'])

        self.tool_bar = ToolBar(self)
        self.add(self.tool_bar)
        self.main_display_frame = MainDisplayFrame(self)
        self.add(self.main_display_frame)
        
        

        
