from PySide6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QMessageBox,QLabel,QLineEdit,QHBoxLayout,QTabWidget,QApplication
from PySide6.QtCore import Qt, QTimer,QEvent
import sys

class mainwindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app=app#initializes app
        self.setWindowTitle("Project_N📕")#sets title
        menu=self.menuBar()
        menu.setNativeMenuBar(False)
        account=menu.addMenu("Account")
        account.addAction("Profile")
        account.addAction("Privacy Policies")

app=QApplication(sys.argv)
window=mainwindow(app)
window.show()
app.exec()


