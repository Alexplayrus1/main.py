from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


import sys


class mainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(mainWindow,self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))

        self.setCentralWidget(self.browser)

        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        fr_btn = QAction('>', self)
        fr_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fr_btn)

        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)


app = QApplication(sys.argv)
app.setApplicationName("GDev NET PY")
window = mainWindow()

app.exec_()
