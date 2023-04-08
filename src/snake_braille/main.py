# SPDX-FileCopyrightText: 2023-present Michael Whapples <mwhapples@aim.com>
#
# SPDX-License-Identifier: GPL-3.0-only
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit
from snake_braille.braille_keyboard import BrailleKeyboardFilter


def main():
    app = QApplication(sys.argv)
    w = QMainWindow()
    e = QPlainTextEdit(parent=w)
    f = BrailleKeyboardFilter(parent=app)
    app.installEventFilter(f)
    w.setCentralWidget(e)
    w.show()
    sys.exit(app.exec())
