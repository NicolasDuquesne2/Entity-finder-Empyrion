from tkinter import VERTICAL, TOP, BOTH, Y, HORIZONTAL

class ConfigsParams():
    def __init__(self):
        self.config_main_browser_panedwindow = {'orient': VERTICAL, 
                                                'height': 400, 
                                                'width': 1000, 
                                                "side": TOP, 
                                                'expand': Y, 
                                                'fill': BOTH,
                                                'pady': 0,
                                                'padx': 0}
        self.config_main_data_panedwindow = {'orient': VERTICAL, 
                                                'height': 400, 
                                                'width': 1000, 
                                                "side": TOP, 
                                                'expand': Y, 
                                                'fill': BOTH,
                                                'pady': 0,
                                                'padx': 0}
        self.config_main_display_panedwindow = {'orient': HORIZONTAL, 
                                                'height': 400, 
                                                'width': 1000, 
                                                "side": TOP, 
                                                'expand': Y, 
                                                'fill': BOTH,
                                                'pady': 0,
                                                'padx': 0}
        self.config_listbox_panedwindow = {'orient': VERTICAL, 
                                                'height': 400, 
                                                'width': 200, 
                                                "side": TOP, 
                                                'expand': Y, 
                                                'fill': BOTH,
                                                'pady': 10,
                                                'padx': 0}
        self.config_treeview_panedwindow = {'orient': VERTICAL, 
                                                'height': 400, 
                                                'width': 900, 
                                                "side": TOP, 
                                                'expand': Y, 
                                                'fill': BOTH,
                                                'pady': 10,
                                                'padx': 0}
        self.config_search_bar = {'height': 100, 
                                  'width': 35}
        self.config_tool_bar = {'width': 1000,
                                'height': 100,
                                'fill': BOTH,
                                'padx': 2,
                                'pady': 15}
        self.config_listbox = {'width': 100}
        self.config_treeview = {'columns': [{'name': 'one', 'width':100, 'minwidth': 100, 'text': "Nom entité", 'anchor': 'center'},
                                            {'name': 'two','width':250, 'minwidth': 100, 'text': "Nom secteur", 'anchor': 'center'},
                                            {'name': 'three','width':250, 'minwidth': 100, 'text':"Nom système", 'anchor': 'center'}],
                                'show': 'headings'}
