import sys
from PySide2.QtWidgets import QApplication
from MainWindow import MainWindow



if __name__ == "__main__":


    # Qt Application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())