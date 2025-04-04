from PyQt5.QtWidgets import QFileDialog
from siui.components import (
    SiPushButton, 
    SiTitledWidgetGroup,
    SiOptionCardPlane,
    )
import re
from siui.core import Si, SiColor, SiGlobal,GlobalFont
from siui.components.page.child_page import SiChildPage
from .DemoLabel import DemoLabel
from .side_message import send_simple_message
from ..json_changer import json_rewriter
from ..FolderMover import FolderMover


class ChildPage_ProjectDetail(SiChildPage):
    def __init__(self,parent):
        super().__init__(parent)

        self.view().setMinimumWidth(800)
        self.content().setTitle("项目管理")
        self.content().setPadding(64)
        self.project_path="project_path"
        self.project_name="Bert"

        # self.project_path=project_path
        # self.project_name=project_name
        self.parent=parent
        self.changed_path=None

        # page content
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            self.option_card_general = SiOptionCardPlane(self)
            self.option_card_general.setTitle("项目位置设置")

            self.button2 = SiPushButton(self)
            self.button2.setFixedHeight(32)
            self.button2.attachment().setText("更改安装位置")
            self.button2.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
            self.button2.clicked.connect(self.openFolderDialog)

            self.option_card_general.body().setAdjustWidgetsSize(True)
            self.option_card_general.body().addWidget(DemoLabel(self,f"当前项目根目录为{self.project_path}",""))
            self.option_card_general.body().addWidget(DemoLabel(self,f"当前项目启动bat为{self.project_path}\launch.bat",""))
            self.option_card_general.body().addWidget(self.button2)
            self.option_card_general.body().addPlaceholder(12)
            self.option_card_general.adjustSize()

            group.addWidget(self.option_card_general)

        self.content().setAttachment(self.titled_widget_group)

        # control panel
        self.demo_button = SiPushButton(self)
        self.demo_button.resize(128, 32)
        self.demo_button.attachment().setText("保存")
        self.demo_button.clicked.connect(self.closeParentLayer)

        self.demo_button.clicked.connect(lambda: self.onSaveButtomClicked(self.parent))

        self.panel().addWidget(self.demo_button, "right")

        # load style sheet
        SiGlobal.siui.reloadStyleSheetRecursively(self)

    def onSaveButtomClicked(self,parent):
        if self.changed_path!=None:
            self.folder_Mover=FolderMover(self.project_path,self.changed_path)
            self.folder_Mover.progress_updated.connect(parent.presentage_updated)

            json_rewriter(self.project_name,self.changed_path)

    def openFolderDialog(self):
    # 打开文件夹选择对话框
        folder_path = QFileDialog.getExistingDirectory(self, "选择安装位置")
        if folder_path:
            # 检查路径中是否包含中文或空格
            if re.search(r'[\u4e00-\u9fff\s]', (folder_path)):
                send_simple_message(4, "路径中不能包含中文或空格，请重新选择。" ,True, 100000)
                self.demo_button.setEnabled(False)

            else:
                self.changed_path = folder_path.replace("/", "\\")
                self.button2.attachment().setText(f"更改安装位置为{self.changed_path}")
                self.demo_button.setEnabled(True)
