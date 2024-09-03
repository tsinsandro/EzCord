import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QSystemTrayIcon

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()

        # Load the URL
        url = QUrl("https://discord.com/app")
        self.browser.setUrl(url)

        # Set the central widget of the Window
        self.setCentralWidget(self.browser)
        
        # Set the window title
        self.setWindowTitle("Discord Browser")
        
        # Maximize the window
        self.showMaximized()

        # Inject the custom button into the web page
        self.browser.page().loadFinished.connect(self.inject_button)

        # Set up the system tray icon
        self.tray_icon = QSystemTrayIcon(QIcon(), self)
        self.tray_icon.setToolTip("Discord Browser")
        self.tray_icon.show()

    def inject_button(self):
        # JavaScript code to inject a button into the webpage
        js_code = """
            (function() {
                // Create a button element
                var button = document.createElement('button');
                button.innerHTML = 'ℹ';
                button.id = 'authorInfoButton';
                button.style.position = 'fixed';
                button.style.top = '10px';
                button.style.right = '10px';
                button.style.zIndex = '1000';
                button.style.backgroundColor = '#DBDEE1';  // Background color
                button.style.border = 'none';
                button.style.borderRadius = '50%';  // Make the button round
                button.style.width = '30px';  // Adjust size
                button.style.height = '30px';  // Adjust size
                button.style.display = 'flex';
                button.style.alignItems = 'center';
                button.style.justifyContent = 'center';
                button.style.cursor = 'pointer';
                button.title = 'About the Author';
                button.style.fontSize = '20px';  // Adjust icon size
                button.style.color = '#303338';  // Icon color

                // Add the button to the body
                document.body.appendChild(button);

                // Add click event listener
                button.addEventListener('click', function() {
                    alert('Made with ❤️ by Aleksandre Tsintsadze');
                });
            })();
        """
        self.browser.page().runJavaScript(js_code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
