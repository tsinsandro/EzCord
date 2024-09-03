
# ███████╗███████╗░█████╗░░█████╗░██████╗░██████╗░
# ██╔════╝╚════██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
# █████╗░░░░███╔═╝██║░░╚═╝██║░░██║██████╔╝██║░░██║
# ██╔══╝░░██╔══╝░░██║░░██╗██║░░██║██╔══██╗██║░░██║
# ███████╗███████╗╚█████╔╝╚█████╔╝██║░░██║██████╔╝
# ╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()

        url = QUrl("https://discord.com/app")
        self.browser.setUrl(url)
        
        # Set the central widget of the Window
        self.setCentralWidget(self.browser)
        
        # Title
        self.setWindowTitle("EzCord Client")
        
        # Maximize the window
        self.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
