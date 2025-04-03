from PyQt5.QtWidgets import QFileDialog
from siui.components import (
    SiLabel,
    SiDenseHContainer,
    SiDividedHContainer,
    SiDividedVContainer,
    SiFlowContainer,
    SiDraggableLabel, 
    SiSimpleButton, 
    SiPushButton, 
    SiMasonryContainer,
    SiCircularProgressBar,
    SiDenseVContainer,
    SiLineEditWithDeletionButton,
    SiLineEditWithItemName,
    SiOptionCardLinear,
    SiTitledWidgetGroup,
    SiOptionCardPlane,
    SiWidget,
    )
from siui.core import Si, SiColor, SiGlobal,GlobalFont
from siui.components.page.child_page import SiChildPage
from .DemoLabel import DemoLabel




class ChildPage_ProjectDetail(SiChildPage):
    def __init__(self,parent,project_path):
        super().__init__(parent)

        self.view().setMinimumWidth(800)
        self.content().setTitle("项目管理")
        self.content().setPadding(64)
        self.project_path=project_path
        self.changed_path=""

        # page content
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            self.option_card_general = SiOptionCardPlane(self)
            self.option_card_general.setTitle("启动设置")


            self.option_card_general.body().setAdjustWidgetsSize(True)
            self.option_card_general.body().addWidget(DemoLabel(self,f"当前项目根目录为{self.project_path}",""))
            self.option_card_general.body().addWidget(DemoLabel(self,f"当前项目启动bat为{self.project_path}\launch.bat",""))
            self.option_card_general.body().addPlaceholder(12)
            self.option_card_general.adjustSize()

            button2 = SiPushButton(self)
            button2.setFixedHeight(32)
            button2.attachment().setText("更改安装位置")
            button2.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
            button2.clicked.connect(self.openFolderDialog)

            group.addWidget(self.option_card_general)

        self.content().setAttachment(self.titled_widget_group)

        # control panel
        self.demo_button = SiPushButton(self)
        self.demo_button.resize(128, 32)
        self.demo_button.attachment().setText("保存")
        self.demo_button.clicked.connect(self.closeParentLayer)

        self.panel().addWidget(self.demo_button, "right")

        # load style sheet
        SiGlobal.siui.reloadStyleSheetRecursively(self)

def openFolderDialog(self):
    # 打开文件夹选择对话框
    folder_path = QFileDialog.getExistingDirectory(self, "更改安装位置")
    if folder_path:
        self.changed_path = folder_path
