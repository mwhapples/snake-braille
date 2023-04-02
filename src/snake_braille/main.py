# SPDX-FileCopyrightText: 2023-present Michael Whapples <mwhapples@aim.com>
#
# SPDX-License-Identifier: GPL-3.0-only
import sys
from PySide6.QtWidgets import QApplication, QPlainTextEdit, QMainWindow


def main():
    app = QApplication(sys.argv)
    w = QMainWindow()
    e = QPlainTextEdit(parent=w)
    w.setCentralWidget(e)
    w.show()
    sys.exit(app.exec())
