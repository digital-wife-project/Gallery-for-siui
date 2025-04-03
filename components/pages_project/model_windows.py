from ast import Lambda
from PyQt5.QtCore import pyqtSignal
from siui.components import SiLabel, SiLongPressButton, SiPushButton
from siui.core import SiColor, SiGlobal
from PyQt5.QtWidgets import QFileDialog

from siui.templates.application.components.dialog.modal import SiModalDialog

from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QBoxLayout, QWidget

from siui.components import SiDenseHContainer, SiDenseVContainer, SiTitledWidgetGroup
from siui.components.button import (
    SiFlatButton,
    SiLongPressButtonRefactor,
    SiProgressPushButton,
    SiPushButtonRefactor,
    SiRadioButtonR,
    SiRadioButtonWithAvatar,
    SiRadioButtonWithDescription,
    SiSwitchRefactor,
    SiToggleButtonRefactor,
)
from siui.components.chart import SiTrendChart
from siui.components.container import SiDenseContainer, SiTriSectionPanelCard, SiTriSectionRowCard
from siui.components.editbox import SiCapsuleEdit, SiDoubleSpinBox, SiLineEdit, SiSpinBox
from siui.components.label import SiLinearIndicator
from siui.components.page import SiPage
from siui.components.slider_ import SiCoordinatePicker2D, SiCoordinatePicker3D, SiSlider
from siui.core import SiGlobal
from siui.gui import SiFont

from ..option_card import OptionCardPlaneForWidgetDemos


class ModalDownloadDialog(SiModalDialog):


    def __init__(self,parent,file_name):
        super().__init__(parent)
        self.setFixedWidth(500)
        self.file_name=file_name
        self.user_path = ""

        self.icon().load(SiGlobal.siui.iconpack.get("ic_fluent_save_filled",
                                                    color_code=SiColor.mix(
                                                        self.getColor(SiColor.SVG_NORMAL),
                                                        self.getColor(SiColor.INTERFACE_BG_B),
                                                        0.05))
                         )

        label = SiLabel(self)
        label.setStyleSheet(f"color: {self.getColor(SiColor.TEXT_E)}")
        label.setText(
            f'<span style="color: {self.getColor(SiColor.TEXT_B)}">选择项目{self.file_name}的安装位置</span><br>'
        )
        label.adjustSize()
        self.contentContainer().addWidget(label)

        button1 = SiPushButton(self)
        button1.setFixedHeight(32)
        button1.attachment().setText("使用默认位置")
        button1.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button1.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)


        button2 = SiPushButton(self)
        button2.setFixedHeight(32)
        button2.attachment().setText("自定义安装位置")
        button2.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button2.clicked.connect(self.openFolderDialog)

        button3 = SiPushButton(self)
        button3.setFixedHeight(32)
        button3.attachment().setText("开始下载与安装")
        button3.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button3.clicked.connect(lambda: self.on_download_click(parent))
        button3.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        button4 = SiPushButton(self)
        button4.setFixedHeight(32)
        button4.attachment().setText("取消")
        button4.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button4.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        self.buttonContainer().addWidget(button1)
        self.buttonContainer().addWidget(button2)
        self.buttonContainer().addWidget(button3)
        self.buttonContainer().addWidget(button4)
        SiGlobal.siui.reloadStyleSheetRecursively(self)
        self.adjustSize()

    def on_download_click(self,parent):
        if self.user_path=="":
            self.user_path="./project/"
        parent.on_download_click.emit(self.file_name,self.user_path)

    def openFolderDialog(self):
        # 打开文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择安装位置")
        if folder_path:
            self.user_path = folder_path





