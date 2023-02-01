from tools.databases import Database
from views.mainwindow import Mainwindow

"""
Start file :
Sets print commande for a log file txt
Open the config data base
Then open automaticaly the last valid data base
initiates the app and binds the open database
then mainloop()
"""

"""sys.stdout = open('errorslog.text', 'w') """
app = Mainwindow()
app.title("Entity empyrion finder")
app.mainloop()
