import src.pages.login_page
import src.pages.create_account
from PyQt6.QtWidgets import QApplication
from sys import argv


# initiates the login_page window from the src.pages.login_page
def main():
    app = QApplication(argv)
    try:
        login_page = src.pages.login_page.LoginPage()
        login_page.show()
        login_page.showMaximized()
        app.exec()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
