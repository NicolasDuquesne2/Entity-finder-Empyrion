from tkinter import PanedWindow
from tools.configs import ConfigsParams
from views.listboxframe import ListBoxFrame
from views.treeviewframe import TreeViewFrame

class MainDisplayFrame(PanedWindow):

    def __init__(self, parent):
        self.config_main_display_panedwindow = ConfigsParams().config_main_display_panedwindow

        PanedWindow.__init__(self, parent, orient= self.config_main_display_panedwindow['orient'], 
                            height=self.config_main_display_panedwindow['height'],
                            width=self.config_main_display_panedwindow['width'])
        
        self.pack(side=self.config_main_display_panedwindow['side'], 
                    expand=self.config_main_display_panedwindow['expand'], 
                    fill=self.config_main_display_panedwindow['fill'], 
                    pady=self.config_main_display_panedwindow['pady'], 
                    padx=self.config_main_display_panedwindow['padx'])

        self.tree_view_frame = TreeViewFrame(self)
        self.list_box_frame = ListBoxFrame(self)
        self.list_box_frame.list_box.add_observer(self.tree_view_frame.tree_view)
        self.add(self.list_box_frame)
        self.add(self.tree_view_frame)