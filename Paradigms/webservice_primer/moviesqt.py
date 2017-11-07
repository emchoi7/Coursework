
import sys
from PyQt4 import QtGui
from PyQt4.Qt import *
from PyQt4.QtCore import *
import requests
import json


class MoviesQT(QMainWindow):
    def __init__(self):
        super(MoviesQT, self).__init__()
        self.setWindowTitle("Movie Recommender")

        #set central widget
        self.central = MoviesCentral(parent = self) 
        self.setCentralWidget(self.central)
        #add File menu
        self.filemenu = self.menuBar().addMenu("File")
        fileExitAction = QAction("Exit", self)
        self.filemenu.addAction(fileExitAction) 
        
        #add User menu
        self.filemenu = self.menuBar().addMenu("User")
        fileViewProfile = QAction("View Profile", self)
        fileSetUser = QAction("Set User", self)
        self.filemenu.addAction(fileViewProfile)
        self.filemenu.addAction(fileSetUser)

        #exit
        self.connect(fileExitAction, SIGNAL("triggered()"), self.exit_program)

        #view profile
        self.connect(fileViewProfile, SIGNAL("triggered()"), self.user_info)

        #set user
        self.connect(fileSetUser, SIGNAL("triggered()"), self.set_user)

    def exit_program(self):
        app.quit()
    	
    def set_user(self):
    	text, ok = QInputDialog.getText(self, 'Input Dialog', 'uid: ')
    	if ok:
    			if text.isdigit:
    				self.central.uid = text
    				self.central.update()

    def user_info(self):
        setuser = QMessageBox()
        r = requests.get(self.central.USERS_URL + str(self.central.uid))
        resp = json.loads(r.content.decode())
        info = "Profile:\nZipcode: {}\nGender: {}\nAge: {}\n".format(resp['zipcode'], resp['gender'], resp['age'])
        setuser.setText(info)
        ret = setuser.exec_()
        self.central.update()

class MoviesCentral(QWidget):
    def __init__(self, parent=None):
        super(MoviesCentral, self).__init__(parent)
        self.uid = 20
        self.SITE_URL = 'http://student04.cse.nd.edu:51001'
        self.USERS_URL = self.SITE_URL + '/users/'
        self.MOVIES_URL = self.SITE_URL + '/movies/'
        self.RESET_URL = self.SITE_URL + '/reset/'
        self.RECOMMENDATIONS_URL = self.SITE_URL + '/recommendations/'
        self.RATING_URL = self.SITE_URL + '/ratings/'
        self.IMAGE_DIR = '/home/paradigms/images'
        self.mid = self.nextRecommendation()

        #generate dict from given movie
        self.resp = self.get_movie()
        self.ratings = self.get_ratings()

        #showing an image
        self.image = QImage(self.IMAGE_DIR + self.resp['img'])
        self.imageLabel = QLabel('no image')
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))


        #labels on GUI
        self.title = QLabel(self.resp['title'])
        self.genre = QLabel(self.resp['genres'])
        self.rating = QLabel(str(self.ratings['rating'])[:3])
        
        #buttons
        self.upbutton = QPushButton("Up") #up button
        self.downbutton = QPushButton("Down") #down button

        #layout
        vlayout = QVBoxLayout() #for title, image, genre, rating
        layout = QHBoxLayout() #up button, CENTER, down button

        vlayout.addWidget(self.title)
        vlayout.addWidget(self.imageLabel)
        vlayout.addWidget(self.genre, Qt.AlignCenter)
        vlayout.addWidget(self.rating, Qt.AlignCenter)
        layout.addWidget(self.upbutton)
        layout.addLayout(vlayout)
        layout.addWidget(self.downbutton)
        self.setLayout(layout)

        self.connect(self.upbutton, SIGNAL('clicked()'), self.clickUpButton)
        self.connect(self.downbutton, SIGNAL('clicked()'), self.clickDownButton)
        

    def update(self):
    	#generate dict from given movie
        self.mid = self.nextRecommendation()
        self.resp = self.get_movie()
        self.ratings = self.get_ratings()

        #showing an image
        self.image = QImage(self.IMAGE_DIR + self.resp['img'])
        self.imageLabel.setPixmap(QPixmap.fromImage(self.image))

        #labels on GUI
        self.title.setText(self.resp['title'])
        self.genre.setText(self.resp['genres'])
        self.rating.setText(str(self.ratings['rating'])[:4])



    def exit_program(self):
        app.quit()

    def clickUpButton(self):
    	self.ratings['rating'] = 5
    	r = requests.put(self.RECOMMENDATIONS_URL + str(self.uid),data=json.dumps(self.ratings))
    	self.update()

    def clickDownButton(self):
    	self.ratings['rating'] = 1
    	r = requests.put(self.RECOMMENDATIONS_URL + str(self.uid),data=json.dumps(self.ratings))
    	self.update()
#
    def nextRecommendation(self):
        r = requests.get(self.RECOMMENDATIONS_URL + str(self.uid))
        resp = json.loads(r.content.decode())
        return resp['movie_id']

    def get_movie(self):
        r = requests.get(self.MOVIES_URL + str(self.mid))
        resp = json.loads(r.content.decode())
        return resp

    def get_ratings(self):
        r = requests.get(self.RATING_URL + str(self.mid))
        resp = json.loads(r.content.decode())
        return resp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MoviesQT()
    gui.show()
    sys.exit(app.exec_())

