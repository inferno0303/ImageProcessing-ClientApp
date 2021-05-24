import sys

from PyQt5.QtWidgets import QApplication

# 窗口实例
from main_windows import main_window


def main():
    app = QApplication(sys.argv)
    main_window_ = main_window.MainWindow()
    main_window_.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
