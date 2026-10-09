# from PySide6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QMessageBox,QLabel,QLineEdit,QHBoxLayout,QTabWidget,QApplication
# from PySide6.QtCore import Qt, QTimer,QEvent
# import sys
# from projectbackend_settings import SettingsWindow
# class mainwindow(QMainWindow):
#     def __init__(self,app):
#         super().__init__()
#         self.app=app#initializes app
#         self.setWindowTitle("Project_N📕")#sets title
#         menu=self.menuBar()
#         menu.setNativeMenuBar(False)
#         account=menu.addMenu("Account")
#         account.addAction("Profile")
#         account.addAction("Settings",self.open_settings)
#         account.addAction("Privacy Policies")
#     def open_settings(self):
#       app = QApplication.instance()
#       wns_app = app is None
#       if wns_app:                      # running settings.py by itself
#            app = QApplication(sys.argv)

#            w = SettingsWindow(on_saved=self.apply_settings)
#            w.show()

#       if wns_app:                      # only start an event loop if we made the app
#            sys.exit(app.exec())
#            return w            
   
 
# app=QApplication(sys.argv)
# window=mainwindow(app)
# window.show()
# app.exec()


from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QSettings
import sys
from projectbackend_settings import SettingsWindow


class mainwindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.settings_window = None              # keeps the window alive
        self.setWindowTitle("Project_N📕")

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        account = menu.addMenu("Account")
        account.addAction("Profile")
        account.addAction("Settings", self.open_settings)   # no parentheses
        account.addAction("Privacy Policies")

    def open_settings(self):
        if self.settings_window is None or not self.settings_window.isVisible():
            self.settings_window = SettingsWindow(on_saved=self.apply_settings)
            self.settings_window.show()
        else:
            self.settings_window.raise_()
            self.settings_window.activateWindow()

    def apply_settings(self):
        s = QSettings("abhi", "Project_N")
        print("Saved focus minutes:", int(s.value("minutes", 25)))


app = QApplication(sys.argv)
window = mainwindow(app)
window.show()
sys.exit(app.exec())