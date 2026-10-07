from PySide6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QMessageBox,QLabel,QLineEdit,QHBoxLayout,QTabWidget,QApplication
from PySide6.QtCore import Qt, QTimer,QEvent
import sys

class mainwindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app=app
        self.setWindowTitle("Project_N📕")
        menu=self.menuBar()
        menu.setNativeMenuBar(False)
        account=menu.addMenu("account")
        account.addAction(print("hello"))
        settings=menu.addMenu("Settings")
        settings.addAction(print("Bye"))
        

app=QApplication(sys.argv)
window=mainwindow(app)
window.show()
app.exec()


