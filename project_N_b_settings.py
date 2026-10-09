from PySide6.QtWidgets import QMainWindow,QWidget,QPushButton,QVBoxLayout,QMessageBox,QLabel,QLineEdit,QHBoxLayout,QTabWidget,QApplication
from PySide6.QtCore import Qt, QTimer,QEvent
import sys
# class mainwindow(QMainWindow):
#     def __init__(self,app):
#         super().__init__()
#         self.app=app
#         self.setWindowTitle("Setings")
#         layout=self.QVBoxLayout()
        









# app=QApplication(sys.argv)
# window=mainwindow(app)
# window.show()
# app.exec()


from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QApplication
from PySide6.QtCore import Qt, QSettings
import sys
from PySide6.QtWidgets import QCheckBox, QButtonGroup


class SettingsWindow(QWidget):
    def __init__(self, on_saved=None):
        super().__init__()
        self.setStyleSheet(STYLE)
        self.on_saved = on_saved
        self.setWindowTitle("Settings")
        self.resize(350, 120)
        self.settings = QSettings("abhi", "Project_N")

        layout = QVBoxLayout(self)
        

        # --- slider row: [label] [slider] [value] ---
        col=QVBoxLayout()
        col.addWidget(QLabel("""Account Setiing
                                Pomodoro settings"""))
        self.easy=QCheckBox("Easy (short duration 25:5)")
        self.medium=QCheckBox("Medium(good for people woth hiher focus,60:10)")
        self.hard=QCheckBox("Hard,you know what it is ,(120:20)")
        self.group1=QButtonGroup(self)
        self.group1.setExclusive(True) 
        self.group1.addButton(self.easy, 2)
        self.group1.addButton(self.medium, 3)
        self.group1.addButton(self.hard, 4)
        self.easy.setChecked(True)
        col.addWidget(self.easy)
        col.addWidget(self.medium)
        col.addWidget(self.hard)
        layout.addLayout(col)
        ############################################
        self.option1=QCheckBox("Check1 will add somethimg")
        self.option2=QCheckBox("Check2 will add somethimg")
        self.option3=QCheckBox("Check3 will add somethimg")
        self.option4=QCheckBox("Check4 will add somethimg")
        self.option5=QCheckBox("Check5 will add somethimg add yours")
        self.option6=QCheckBox("Check6 will add somethimg u could add animated")
        self.group2=QButtonGroup(self)
        self.group2.setExclusive(True)
        self.group2.addButton(self.option1,5)
        self.group2.addButton(self.option2,6)
        self.group2.addButton(self.option3,7)
        self.group2.addButton(self.option4,8)
        self.group2.addButton(self.option5,9)
        self.group2.addButton(self.option6,10)
        self.option1.setChecked(True)
        #####
        col.addWidget(QLabel("Bg_options:"))
        setcol=QHBoxLayout()
        vol1=QVBoxLayout()
        vol2=QVBoxLayout()
        vol1.addWidget(self.option1)
        vol1.addWidget(self.option2)
        vol1.addWidget(self.option3)
        vol2.addWidget(self.option4)
        vol2.addWidget(self.option5)
        vol2.addWidget(self.option6)

       

        setcol.addLayout(vol1)
        setcol.addLayout(vol2)
        layout.addLayout(setcol)


        ############################################################
        row = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(1, 60)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.value_label = QLabel(
        )

        row.addWidget(QLabel("Focus:"))
        row.addWidget(self.slider, 1)          # slider takes the extra space
        row.addWidget(self.value_label)
        layout.addLayout(row)

        # connect, then load the saved value
        self.slider.valueChanged.connect(self.update_label)
        self.slider.setValue(int(self.settings.value("minutes", 25)))
        self.update_label(self.slider.value())

    def update_label(self, value):
        self.value_label.setText(f"{value} min")

    def closeEvent(self, event):               # X = save
        self.settings.setValue("minutes", self.slider.value())
        if self.on_saved:
            self.on_saved()
        event.accept()
    # settings.py
              # caller must keep this reference

STYLE = """
QWidget {
    background-color: #1c1c1f;
    color: #f2f2f7;
    font-family: "SF Pro Text", "Helvetica Neue", sans-serif;
    font-size: 14px;
}

/* Section headings */
QLabel#sectionTitle {
    font-size: 13px;
    font-weight: 600;
    color: #8e8e93;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Checkboxes */
QCheckBox {
    spacing: 10px;
    padding: 6px 0;
}
QCheckBox::indicator {
    width: 18px;
    height: 18px;
    border-radius: 5px;
    border: 1.5px solid #48484a;
    background: #0054E1;
}
QCheckBox::indicator:hover {
    border-color: #0a84ff;
}
QCheckBox::indicator:checked {
    background: #0a84ff;
    border-color: #0a84ff;
    image: url(check.svg);   /* optional white tick icon */
}

/* Slider */
QSlider::groove:horizontal {
    height: 6px;
    background: #3a3a3c;
    border-radius: 3px;
}
QSlider::sub-page:horizontal {
    background: #0a84ff;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background: white;
    width: 20px;
    height: 20px;
    margin: -7px 0;          /* centers handle on groove */
    border-radius: 10px;
}
QSlider::handle:horizontal:hover {
    background: #e5e5ea;
}
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SettingsWindow()
    w.show()
    sys.exit(app.exec())