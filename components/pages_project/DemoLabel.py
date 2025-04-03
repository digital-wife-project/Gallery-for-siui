from PyQt5.QtCore import Qt, pyqtSignal
from siui.components import (
    SiLabel,
    )
from siui.core import Si, SiColor


class DemoLabel(SiLabel):
    def __init__(self, parent, text,hint):
        super().__init__(parent)

        self.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(32)

        self.setFixedStyleSheet("border-radius: 4px")
        self.setText(text)
        self.setHint(hint)
        self.adjustSize()
        self.resize(self.width() + 24, self.height())

    def reloadStyleSheet(self):
        self.setStyleSheet(f"color: {self.getColor(SiColor.TEXT_B)};"
                           f"background-color: {self.getColor(SiColor.INTERFACE_BG_D)}")

