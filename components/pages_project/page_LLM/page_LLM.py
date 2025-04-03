from PyQt5.QtCore import Qt

from siui.components import SiTitledWidgetGroup, SiLabel, SiDenseHContainer, SiDenseVContainer, SiDividedHContainer, \
    SiDividedVContainer, SiFlowContainer, SiDraggableLabel, SiSimpleButton, SiPushButton, SiMasonryContainer
from siui.components.page import SiPage
from siui.core import SiColor, GlobalFont
from siui.core import SiGlobal
from siui.core import Si
from siui.gui import SiFont
from ... option_card import OptionCardPlaneForWidgetDemos

import random


class DemoLabel(SiLabel):
    def __init__(self, parent, text):
        super().__init__(parent)

        self.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedHeight(32)

        self.setFixedStyleSheet("border-radius: 4px")
        self.setText(text)
        self.adjustSize()
        self.resize(self.width() + 24, self.height())

    def reloadStyleSheet(self):
        self.setStyleSheet(f"color: {self.getColor(SiColor.TEXT_B)};"
                           f"background-color: {self.getColor(SiColor.INTERFACE_BG_D)}")




class LLM(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.message_type = 0
        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)

        # 创建控件组
        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSpacing(32)
        self.titled_widgets_group.setAdjustWidgetsSize(True)

        # 密堆积容器
        with self.titled_widgets_group as group:
            # 竖直密堆积容器
            self.dense_v_container = OptionCardPlaneForWidgetDemos(self)
            # self.dense_v_container.setSourceCodeURL("https://github.com/ChinaIceF/PyQt-SiliconUI/blob/main/siui/components"
            #                                         "/widgets/progress_bar/progress_bar.py")
            self.dense_v_container.setTitle("竖直密堆积容器")

            self.demo_dense_v_container = SiDenseVContainer(self)
            self.demo_dense_v_container.setFixedHeight(300)
            self.demo_dense_v_container.addWidget(DemoLabel(self, "顶侧A"), "top")
            self.demo_dense_v_container.addWidget(DemoLabel(self, "顶侧B"), "top")
            self.demo_dense_v_container.addWidget(DemoLabel(self, "..."), "top")
            self.demo_dense_v_container.addWidget(DemoLabel(self, "底侧A"), "bottom")
            self.demo_dense_v_container.addWidget(DemoLabel(self, "底侧B"), "bottom")
            self.demo_dense_v_container.addWidget(DemoLabel(self, "..."), "bottom")

            self.dense_v_container.body().addWidget(self.demo_dense_v_container)
            self.dense_v_container.body().addPlaceholder(12)
            self.dense_v_container.adjustSize()

            # group.addWidget(self.dense_h_container)
            group.addWidget(self.dense_v_container)
        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)
