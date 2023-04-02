# SPDX-FileCopyrightText: 2023-present Michael Whapples <mwhapples@aim.com>
#
# SPDX-License-Identifier: GPL-3.0-only
from types import MappingProxyType
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QPlainTextEdit

DOTS_TO_UNICODE = tuple([chr(x) for x in range(0x2800, 0x2900)])

QWERTY_SIX_KEYS = MappingProxyType({
    Qt.Key.Key_F: 0x1,
    Qt.Key.Key_D: 0x2,
    Qt.Key.Key_S: 0x4,
    Qt.Key.Key_J: 0x8,
    Qt.Key.Key_K: 0x10,
    Qt.Key.Key_L: 0x20
})


class SixKeyEdit(QPlainTextEdit):
    def __init__(self, dots_to_char=DOTS_TO_UNICODE, key_to_dots=QWERTY_SIX_KEYS, parent=None):
        super().__init__(parent)
        self._dots = 0
        self._key_state = 0
        self._key_to_dots = key_to_dots
        self._dots_to_char = dots_to_char

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if self._braille_handle_key_event(e):
            if e.key() in self._key_to_dots:
                key_dot = self._key_to_dots[e.key()]
                self._dots |= key_dot
                self._key_state |= key_dot
        else:
            super().keyPressEvent(e)

    @staticmethod
    def _braille_handle_key_event(e):
        key_text = e.text()
        modifiers = e.keyCombination().keyboardModifiers()
        return ((modifiers == Qt.KeyboardModifier.NoModifier or modifiers == Qt.KeyboardModifier.ShiftModifier) and
                e.key() != Qt.Key.Key_Space and key_text and key_text.isprintable())

    def keyReleaseEvent(self, e: QKeyEvent) -> None:
        if self._braille_handle_key_event(e):
            if e.key() in self._key_to_dots:
                key_dot = self._key_to_dots[e.key()] ^ 0xff
                self._key_state &= key_dot
            if not self._key_state:
                self.insertPlainText(self._dots_to_char[self._dots & 0xff])
                self._dots = 0
