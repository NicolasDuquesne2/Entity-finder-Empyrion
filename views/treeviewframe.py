from tkinter import PanedWindow
from tools.configs import ConfigsParams
from views.treeview import TreeView

class TreeViewFrame(PanedWindow):

    def __init__(self, parent):
        self.config_treeview_panedwindow = ConfigsParams().config_treeview_panedwindow

        PanedWindow.__init__(self, parent, orient= self.config_treeview_panedwindow['orient'], 
                            height=self.config_treeview_panedwindow['height'],
                            width=self.config_treeview_panedwindow['width'])
        
        self.pack(side=self.config_treeview_panedwindow['side'], 
                  expand=self.config_treeview_panedwindow['expand'], 
                  fill=self.config_treeview_panedwindow['fill'], 
                  pady=self.config_treeview_panedwindow['pady'], 
                  padx=self.config_treeview_panedwindow['padx'])
        
        self.tree_view = TreeView(self)
        self.add(self.tree_view)
