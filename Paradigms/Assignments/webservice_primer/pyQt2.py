import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        self.central = Form(parent=self)
        self.setCentralWidget(self.central)

        self.filemenu = self.menuBar().addMenu("File")
        fileExitAction = QAction("Exit", self)
        self.filemenu.addAction(fileExitAction)

        self.connect(fileExitAction, SIGNAL("triggered()"), self.exit_program)

    def exit_program(self):
        app.quit()

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        print("Form init happened")
        
        #showing an image
        self.image = QImage('/home/paradigms/images/rfZjAdKwceWQxlfFB7Em9XdpoLI.jpg')
        self.imageLabel = QLabel('no image')
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))
        
        self.exitbutton = QPushButton("Exit")

        layout = QHBoxLayout()

        layout.addWidget(self.exitbutton)
        layout.addWidget(self.imageLabel)
        self.setLayout(layout)

        self.connect(self.exitbutton, SIGNAL("clicked()"), self.exit_program)

    def exit_program(self):
        app.quit()



app = QApplication(sys.argv)

form = MyGUI()

form.show()

app.exec_()