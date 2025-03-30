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



class ChildPage_ProjectDetail(SiChildPage):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.view().setMinimumWidth(800)
        self.content().setTitle("项目管理")
        self.content().setPadding(64)

        # page content
        self.titled_widget_group = SiTitledWidgetGroup(self)

        with self.titled_widget_group as group:
            self.option_card_general = SiOptionCardPlane(self)
            self.option_card_general.setTitle("启动设置")

            self.line_edit_title = SiLineEditWithItemName(self)
            self.line_edit_title.setName("项目根目录")
            self.line_edit_title.setFixedHeight(32)
            # text_content = self.line_edit_title.text()

            self.line_edit_description = SiLineEditWithItemName(self)
            self.line_edit_description.setName("项目启动bat")
            self.line_edit_description.setFixedHeight(32)
            # text_content = self.line_edit_description.text()

            self.option_card_general.body().setAdjustWidgetsSize(True)
            self.option_card_general.body().addWidget(self.line_edit_title)
            self.option_card_general.body().addWidget(self.line_edit_description)
            self.option_card_general.body().addPlaceholder(12)
            self.option_card_general.adjustSize()

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