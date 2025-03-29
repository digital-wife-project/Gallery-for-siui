from PyQt5.QtCore import Qt

from siui.components import SiTitledWidgetGroup, SiLabel, SiDenseHContainer, SiDenseVContainer, SiDividedHContainer, \
    SiDividedVContainer, SiFlowContainer, SiDraggableLabel, SiSimpleButton, SiPushButton, SiMasonryContainer
from siui.components.page import SiPage
from siui.core import SiColor, GlobalFont
from siui.core import SiGlobal
from siui.core import Si
from siui.gui import SiFont
from ... option_card import OptionCardPlaneForWidgetDemos
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

import random


class TTS(SiPage):
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
            self.push_buttons = OptionCardPlaneForWidgetDemos(self)

            container = SiDenseHContainer(self)

            self.demo_progress_button_text = SiProgressPushButton(self)
            self.demo_progress_button_text.setText("启动")
            self.demo_progress_button_text.setToolTip("点击以开始下载或使用")
            self.demo_progress_button_text.clicked.connect(lambda: self.demo_progress_button_text.setProgress(random.random() * 1.3))
            self.demo_progress_button_text.adjustSize()

            self.demo_push_button_text = SiPushButtonRefactor(self)
            self.demo_push_button_text.setText("项目管理")
            self.demo_push_button_text.adjustSize()

            self.demo_label_hinted = SiLabel(self)
            self.demo_label_hinted.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.demo_label_hinted.setText("bert")
            self.demo_label_hinted.setHint("使用 setHint 方法设置工具提示")

            self.demo_label = SiLabel(self)
            self.demo_label.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.demo_label.setText("               ")


            container.addWidget(self.demo_progress_button_text,"right")
            container.addWidget(self.demo_push_button_text,"right")
            container.addWidget(self.demo_label,"left")
            container.addWidget(self.demo_label_hinted,"left")


            self.demo_dense_v_container.addWidget(container)

            self.dense_v_container.body().addWidget(self.demo_dense_v_container)
            self.dense_v_container.body().addPlaceholder(12)
            self.dense_v_container.adjustSize()

            # group.addWidget(self.dense_h_container)
            group.addWidget(self.dense_v_container)
        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)
