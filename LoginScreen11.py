import json
import sys
from tkinter import Widget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi
from User import User
user = User()
class Login(QDialog):
    def __init__(self,user):
        super(Login,self).__init__()
        self.user=user
        loadUi("LoginScreen11.ui",self)
        self.loginButton.clicked.connect(self.gotoMenu)
        self.signUpButton.clicked.connect(self.sign_up_func)
    def gotoMenu(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def login_func(self):
        username=self.username.text()
        print("Succesfully logged in with username : ", username)


    def sign_up_func(self):
        self.user.name = self.username.text()
        user_dict = self.user.readjson()
        user_dict[self.user.name] = {"Level": self.user.level, "Total Time": self.user.totaltime}
        self.user.savejson(user_dict)
        
class Menu(QDialog):
    def __init__(self,user):
        super(Menu, self).__init__()
        self.user=user
        loadUi("MenuScreen.ui", self)
        self.playButton.clicked.connect(self.gotoGame)
        # self.quitButton.clicked.connect(self.exit)
    # def exit(self):

    def gotoGame(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Game(QDialog):
    def __init__(self,user):
        super(Game,self).__init__()
        self.user=user
        loadUi("GameScreen.ui", self)
        self.level.setText("Level: "+str(self.user.level))
        self.backButton.clicked.connect(self.back)
        # self.remainingWLabel.setText(remaining_func())
    def back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
    # def remaining_func(self):
    def show_level(self):
        self.level.setText(self.user.level)
        


app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainWindow=Login(user)
game=Game(user)
menu = Menu(user)
widget.addWidget(mainWindow)
widget.addWidget(menu)
widget.addWidget(game)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")



