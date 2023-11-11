import src.pages.login_page, src.pages.create_account
from PyQt6.QtWidgets import QApplication
from sys import argv, exit


# initiates the login_page window from the src.pages.login_page
def run():
    app = QApplication(argv)
    try:
        login_page = src.pages.login_page.LoginPage()
        login_page.show()
        login_page.showMaximized()
        exit(app.exec())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    run()
