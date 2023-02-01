from tkinter import Frame
from tools.configs import ConfigsParams
from views.combobox import ComboBox
from models.entity import EntityModel


class ToolBar(Frame):

    def __init__(self, parent):
        self.config_params = ConfigsParams().config_tool_bar
        
        Frame.__init__(self, parent, width=self.config_params['width'], 
                       height=self.config_params['height'], 
                       padx=self.config_params['padx'], 
                       pady=self.config_params['pady'])
                       
        self.pack(fill=self.config_params['fill'])
        self.entity_model = EntityModel()
        self.combo_box = ComboBox(self, self.entity_model.entity_types)
        self.combo_box.pack(side="left")