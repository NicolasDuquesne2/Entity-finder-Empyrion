from tkinter.ttk import Treeview
from tools.configs import ConfigsParams
from models.entity import EntityModel

class TreeView(Treeview):
    def __init__(self, parent):
        self.configs = ConfigsParams()
        self.database = None
        self.configs_params = self.configs.config_treeview
        self.columns_params = self.configs_params['columns']
        self.entity_model = EntityModel()

        columns_tuple = ()

        for col in self.columns_params:
            columns_tuple = columns_tuple + (col['name'], )


        Treeview.__init__(self, parent, columns=(columns_tuple), show=self.configs_params['show'])

        for col in self.columns_params:
            self.heading(col['name'], text=col['text'])
            self.column(col['name'], width=col['width'], minwidth=col['minwidth'], anchor=col['anchor'])
        

    """ Loads the tab with datas """
    def populate(self, criteria):
        sql = self.entity_model.get_list_db_entity_by_type(criteria)
        rows = self.database.select(sql, self.database.name)
        if rows:
            for row in rows:
                self.insert('', 'end', text=row[0], values=(row[0], row[1], row[2]))


    """ Erase all datas in the tab """
    def dispopulate(self):
        children = self.get_children()
        for child in children:
            self.delete(child)

    """ At the selection in the left side listbox """
    def update(self, criteria):
        self.dispopulate()
        self.populate(criteria)
    
    """ At the data base update """
    def update_db(self, database):
        self.database = database
        self.dispopulate()