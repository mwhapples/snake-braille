# SPDX-FileCopyrightText: 2023-present Michael Whapples <mwhapples@aim.com>
#
# SPDX-License-Identifier: GPL-3.0-only
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from snake_braille.braille_key import BrailleEdit

def main():
    app = QApplication(sys.argv)
    w = QMainWindow()
    e = BrailleEdit(six_key=True, parent=w)
    w.setCentralWidget(e)
    w.show()
    sys.exit(app.exec())
