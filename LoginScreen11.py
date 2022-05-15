import json
import sys
from tkinter import Widget
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi
from User import User

class Login(QDialog):
    user = User()
    def __init__(self):
        super(Login,self).__init__()
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
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("MenuScreen.ui", self)
        self.playButton.clicked.connect(self.gotoGame)
        # self.quitButton.clicked.connect(self.exit)
    # def exit(self):

    def gotoGame(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Game(QDialog):
    def __init__(self):
        super(Game, self).__init__()
        loadUi("GameScreen.ui", self)
        self.backButton.clicked.connect(self.back)
        # self.level.setText(self.User.user.level)
        # self.remainingWLabel.setText(remaining_func())
    def back(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)
    # def remaining_func(self):
        

    


app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainWindow=Login()
game=Game()
menu = Menu()
widget.addWidget(mainWindow)
widget.addWidget(menu)
widget.addWidget(game)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")



