# -*- coding: utf-8 -*-
import logging
import mistune

from qtpy import QtWidgets, QtCore, QtGui
from pathlib import Path

__all__ = ["Changes"]

logger = logging.getLogger("fastflix")

markdown = mistune.Markdown()


class Changes(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.setMinimumWidth(500)
        self.setMinimumHeight(500)
        # making qwidget object
        content = QtWidgets.QWidget(self)
        self.setWidget(content)
        # vertical box layout
        lay = QtWidgets.QVBoxLayout(content)

        # creating label
        self.label = QtWidgets.QLabel(markdown((Path(__file__).parent.parent / "CHANGES").read_text()))

        # setting alignment to the text
        self.label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    def closeEvent(self, event):
        self.hide()
        # event.accept()