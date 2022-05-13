import json
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.uic import loadUi
import User

class Login(QDialog):
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
        print("merhaba")
        print("merhaba")

    def sign_up_func(self):
        with open(r'C:\Users\Ruben\Desktop\Flash\username.json', 'r') as json_file:
            self.data = json.load(json_file)
        print(self.data)
        user=User()
        user.name=self.username.text()
        self.data[user.name]={"Level":user.level,"Total Time":user.totaltime}
        print(self.data)
        print(type(self.data))
        with open(r'C:\Users\Ruben\Desktop\Flash\username.json','w') as json_file:
            json.dump(self.data, json_file)
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



