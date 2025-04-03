import re
from PyQt5.QtCore import pyqtSignal
from siui.components import SiLabel, SiLongPressButton, SiPushButton
from siui.core import SiColor, SiGlobal
from PyQt5.QtWidgets import QFileDialog

from siui.templates.application.components.dialog.modal import SiModalDialog

from siui.core import SiGlobal

from ..option_card import OptionCardPlaneForWidgetDemos
from .side_message import send_simple_message

class ModalDownloadDialog(SiModalDialog):


    def __init__(self,parent,file_name):
        super().__init__(parent)
        self.setFixedWidth(500)
        self.file_name=file_name
        self.user_path="./project/"

        self.icon().load(SiGlobal.siui.iconpack.get("ic_fluent_save_filled",
                                                    color_code=SiColor.mix(
                                                        self.getColor(SiColor.SVG_NORMAL),
                                                        self.getColor(SiColor.INTERFACE_BG_B),
                                                        0.05))
                         )

        self.label = SiLabel(self)
        self.label.setStyleSheet(f"color: {self.getColor(SiColor.TEXT_E)}")
        self.label.setText(
            f'<span style="color: {self.getColor(SiColor.TEXT_B)}">选择项目的安装位置</span><br>'
            f'<span style="color: {self.getColor(SiColor.TEXT_B)}">当前安装位置{self.user_path}</span><br>'

        )
        self.label.adjustSize()
        self.contentContainer().addWidget(self.label)

        button2 = SiPushButton(self)
        button2.setFixedHeight(32)
        button2.attachment().setText("自定义安装位置")
        button2.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button2.clicked.connect(self.openFolderDialog)

        button3 = SiPushButton(self)
        button3.setFixedHeight(32)
        button3.attachment().setText("开始下载与安装")
        button3.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button3.clicked.connect(lambda: parent.on_download_click.emit(self.file_name,self.user_path))
        button3.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        button4 = SiPushButton(self)
        button4.setFixedHeight(32)
        button4.attachment().setText("取消")
        button4.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button4.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        self.buttonContainer().addWidget(button2)
        self.buttonContainer().addWidget(button3)
        self.buttonContainer().addWidget(button4)
        SiGlobal.siui.reloadStyleSheetRecursively(self)
        self.adjustSize()
        
# lambda: send_custom_message(self.message_type, self.message_auto_close, self.message_auto_close_duration))


    def openFolderDialog(self):
    # 打开文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择安装位置")
        if folder_path:
            # 检查路径中是否包含中文或空格
            if re.search(r'[\u4e00-\u9fff\s]', (folder_path)):
                send_simple_message
                # QMessageBox.warning(self, "警告", "路径中不能包含中文或空格，请重新选择。")
            else:
                self.user_path = folder_path
                self.label.setText(
                    f'<span style="color: {self.getColor(SiColor.TEXT_B)}">选择项目的安装位置</span><br>'
                    f'<span style="color: {self.getColor(SiColor.TEXT_B)}">当前安装位置{self.user_path}</span><br>'

                    )








