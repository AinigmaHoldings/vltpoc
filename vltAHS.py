import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
import os

os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--no-sandbox'
os.environ['QTWEBENGINE_DISABLE_GPU'] = '1'

class Browser(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))  # Convert string to QUrl
        self.setCentralWidget(self.browser)
        self.showFullScreen()  # Show the window in full screen

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #url = 'https://www.loteriastorito.com/toritoganaaltoque'  # Change this URL to the one you want to open
    url = 'https://nexlotlotto.github.io'
    window = Browser(url)
    sys.exit(app.exec_())

