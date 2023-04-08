# SPDX-FileCopyrightText: 2023-present Michael Whapples <mwhapples@aim.com>
#
# SPDX-License-Identifier: GPL-3.0-only
from types import MappingProxyType

from PySide6.QtCore import QEvent, QObject, Qt, QCoreApplication
from PySide6.QtGui import QKeyEvent

QWERTY_BRAILLE_KEYS = MappingProxyType({
    Qt.Key.Key_F: 0x1,
    Qt.Key.Key_D: 0x2,
    Qt.Key.Key_S: 0x4,
    Qt.Key.Key_J: 0x8,
    Qt.Key.Key_K: 0x10,
    Qt.Key.Key_L: 0x20,
    Qt.Key.Key_A: 0x40,
    Qt.Key.Key_Semicolon: 0x80,
    Qt.Key.Key_Space: 0x100
})

_DOTS_KEYS = {
    0x1: (Qt.Key.Key_A, Qt.KeyboardModifier.NoModifier, "a"),
    0x2: (Qt.Key.Key_1, Qt.KeyboardModifier.NoModifier, "1"),
    0x3: (Qt.Key.Key_B, Qt.KeyboardModifier.NoModifier, "b"),
    0x4: (Qt.Key.Key_Apostrophe, Qt.KeyboardModifier.NoModifier, "'"),
    0x5: (Qt.Key.Key_K, Qt.KeyboardModifier.NoModifier, "k"),
    0x6: (Qt.Key.Key_2, Qt.KeyboardModifier.NoModifier, "2"),
    0x7: (Qt.Key.Key_L, Qt.KeyboardModifier.NoModifier, "l"),
    0x8: (Qt.Key.Key_QuoteLeft, Qt.KeyboardModifier.NoModifier, "`"),
    0x9: (Qt.Key.Key_C, Qt.KeyboardModifier.NoModifier, "c"),
    0xa: (Qt.Key.Key_I, Qt.KeyboardModifier.NoModifier, "i"),
    0xb: (Qt.Key.Key_F, Qt.KeyboardModifier.NoModifier, "f"),
    0xc: (Qt.Key.Key_Slash, Qt.KeyboardModifier.NoModifier, "/"),
    0xd: (Qt.Key.Key_M, Qt.KeyboardModifier.NoModifier, "m"),
    0xe: (Qt.Key.Key_S, Qt.KeyboardModifier.NoModifier, "s"),
    0xf: (Qt.Key.Key_P, Qt.KeyboardModifier.NoModifier, "p"),
    0x10: (Qt.Key.Key_QuoteDbl, Qt.KeyboardModifier.NoModifier, "\""),
    0x11: (Qt.Key.Key_E, Qt.KeyboardModifier.NoModifier, "e"),
    0x12: (Qt.Key.Key_3, Qt.KeyboardModifier.NoModifier, "3"),
    0x13: (Qt.Key.Key_H, Qt.KeyboardModifier.NoModifier, "h"),
    0x14: (Qt.Key.Key_9, Qt.KeyboardModifier.NoModifier, "9"),
    0x15: (Qt.Key.Key_O, Qt.KeyboardModifier.NoModifier, "o"),
    0x16: (Qt.Key.Key_6, Qt.KeyboardModifier.NoModifier, "6"),
    0x17: (Qt.Key.Key_R, Qt.KeyboardModifier.NoModifier, "r"),
    0x18: (Qt.Key.Key_AsciiTilde, Qt.KeyboardModifier.NoModifier, "~"),
    0x19: (Qt.Key.Key_D, Qt.KeyboardModifier.NoModifier, "d"),
    0x1a: (Qt.Key.Key_J, Qt.KeyboardModifier.NoModifier, "j"),
    0x1b: (Qt.Key.Key_G, Qt.KeyboardModifier.NoModifier, "g"),
    0x1c: (Qt.Key.Key_Greater, Qt.KeyboardModifier.NoModifier, ">"),
    0x1d: (Qt.Key.Key_N, Qt.KeyboardModifier.NoModifier, "n"),
    0x1e: (Qt.Key.Key_T, Qt.KeyboardModifier.NoModifier, "t"),
    0x1f: (Qt.Key.Key_Q, Qt.KeyboardModifier.NoModifier, "q"),
    0x20: (Qt.Key.Key_Comma, Qt.KeyboardModifier.NoModifier, ","),
    0x21: (Qt.Key.Key_Asterisk, Qt.KeyboardModifier.NoModifier, "*"),
    0x22: (Qt.Key.Key_5, Qt.KeyboardModifier.NoModifier, "5"),
    0x23: (Qt.Key.Key_Less, Qt.KeyboardModifier.NoModifier, "<"),
    0x24: (Qt.Key.Key_Minus, Qt.KeyboardModifier.NoModifier, "-"),
    0x25: (Qt.Key.Key_U, Qt.KeyboardModifier.NoModifier, "u"),
    0x26: (Qt.Key.Key_8, Qt.KeyboardModifier.NoModifier, "8"),
    0x27: (Qt.Key.Key_V, Qt.KeyboardModifier.NoModifier, "v"),
    0x28: (Qt.Key.Key_Period, Qt.KeyboardModifier.NoModifier, "."),
    0x29: (Qt.Key.Key_Percent, Qt.KeyboardModifier.NoModifier, "%"),
    0x2a: (Qt.Key.Key_BraceLeft, Qt.KeyboardModifier.NoModifier, "{"),
    0x2b: (Qt.Key.Key_Dollar, Qt.KeyboardModifier.NoModifier, "$"),
    0x2c: (Qt.Key.Key_Plus, Qt.KeyboardModifier.NoModifier, "+"),
    0x2d: (Qt.Key.Key_X, Qt.KeyboardModifier.NoModifier, "x"),
    0x2e: (Qt.Key.Key_Exclam, Qt.KeyboardModifier.NoModifier, "!"),
    0x2f: (Qt.Key.Key_Ampersand, Qt.KeyboardModifier.NoModifier, "&"),
    0x30: (Qt.Key.Key_Semicolon, Qt.KeyboardModifier.NoModifier, ";"),
    0x31: (Qt.Key.Key_Colon, Qt.KeyboardModifier.NoModifier, ":"),
    0x32: (Qt.Key.Key_4, Qt.KeyboardModifier.NoModifier, "4"),
    0x33: (Qt.Key.Key_Bar, Qt.KeyboardModifier.NoModifier, "|"),
    0x34: (Qt.Key.Key_0, Qt.KeyboardModifier.NoModifier, "0"),
    0x35: (Qt.Key.Key_Z, Qt.KeyboardModifier.NoModifier, "z"),
    0x36: (Qt.Key.Key_7, Qt.KeyboardModifier.NoModifier, "7"),
    0x37: (Qt.Key.Key_ParenLeft, Qt.KeyboardModifier.NoModifier, "("),
    0x38: (Qt.Key.Key_Underscore, Qt.KeyboardModifier.NoModifier, "_"),
    0x39: (Qt.Key.Key_Question, Qt.KeyboardModifier.NoModifier, "?"),
    0x3a: (Qt.Key.Key_W, Qt.KeyboardModifier.NoModifier, "w"),
    0x3b: (Qt.Key.Key_BraceRight, Qt.KeyboardModifier.NoModifier, "}"),
    0x3c: (Qt.Key.Key_NumberSign, Qt.KeyboardModifier.NoModifier, "#"),
    0x3d: (Qt.Key.Key_Y, Qt.KeyboardModifier.NoModifier, "y"),
    0x3e: (Qt.Key.Key_ParenRight, Qt.KeyboardModifier.NoModifier, ")"),
    0x3f: (Qt.Key.Key_Equal, Qt.KeyboardModifier.NoModifier, "="),
    0x40: (Qt.Key.Key_Backspace, Qt.KeyboardModifier.NoModifier, "\x08"),
    0x80: (Qt.Key.Key_Enter, Qt.KeyboardModifier.NoModifier, "\r"),
    0x100: (Qt.Key.Key_Space, Qt.KeyboardModifier.NoModifier, " "),
    0x101: (Qt.Key.Key_Up, Qt.KeyboardModifier.NoModifier, ""),
    0x102: (Qt.Key.Key_Left, Qt.KeyboardModifier.NoModifier, ""),
    0x104: (Qt.Key.Key_Down, Qt.KeyboardModifier.NoModifier, ""),
    0x110: (Qt.Key.Key_Right, Qt.KeyboardModifier.NoModifier, ""),
}


class BrailleKeyEvent(QKeyEvent):
    def __init__(self, eventType, key, modifiers, text, dots):
        super().__init__(eventType, key, modifiers, text)
        self.dots = dots


def createBrailleKeyboardEvents():
    def keyEvents(watched, key, modifiers, text, dots):
        QCoreApplication.sendEvent(watched, BrailleKeyEvent(QEvent.Type.KeyPress, key, modifiers, text, dots))
        QCoreApplication.sendEvent(watched, BrailleKeyEvent(QEvent.Type.KeyRelease, key, modifiers, text, dots))

    return {d: (lambda w, k=k, m=m, t=t, d=d: keyEvents(w, k, m, t, d)) for (d, (k, m, t)) in _DOTS_KEYS.items()}


DOTS_TO_EVENTS = MappingProxyType(createBrailleKeyboardEvents())


class BrailleKeyboardFilter(QObject):
    def __init__(self, keysToDots=QWERTY_BRAILLE_KEYS, parent: QObject = None):
        super().__init__(parent=parent)
        self._keysToDots = keysToDots
        self._dots = 0
        self._keyState = 0

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if not isinstance(event, BrailleKeyEvent):
            if event.type() == QEvent.Type.KeyPress:
                assert isinstance(event, QKeyEvent)
                if event.key() in self._keysToDots:
                    keyDot = self._keysToDots[event.key()]
                    self._dots |= keyDot
                    self._keyState |= keyDot
                    return True
            elif event.type() == QEvent.Type.KeyRelease:
                assert isinstance(event, QKeyEvent)
                if event.key() in self._keysToDots:
                    self._keyState &= self._keysToDots[event.key()] ^ 0xffff
                    if self._keyState == 0:
                        events = DOTS_TO_EVENTS.get(self._dots, lambda w: None)
                        events(watched)
                        self._dots = 0
                    return True
        return super().eventFilter(watched, event)
