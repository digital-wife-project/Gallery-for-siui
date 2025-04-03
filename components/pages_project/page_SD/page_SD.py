from PyQt5.QtCore import Qt

from siui.components import (
    SiDenseVContainer,
    SiTitledWidgetGroup,
    )
from siui.components.page import SiPage
from ... option_card import OptionCardPlaneForWidgetDemos
from ...json_changer import remote_project_json_reader
from ..project_container import Row_for_each_project

import json


class SD(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_type = 0
        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.project_dic=remote_project_json_reader("sd")

        # 创建控件组
        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSpacing(32)
        self.titled_widgets_group.setAdjustWidgetsSize(True)

        # 密堆积容器
        with self.titled_widgets_group as group:
            # 竖直密堆积容器
            self.dense_v_container = OptionCardPlaneForWidgetDemos(self)
            self.dense_v_container.setTitle("竖直密堆积容器")

            self.demo_dense_v_container = SiDenseVContainer(self)
            self.demo_dense_v_container.setFixedHeight(300)
            self.push_buttons = OptionCardPlaneForWidgetDemos(self)

            for key, value in self.project_dic.items():
                self.demo_dense_v_container.addWidget(Row_for_each_project(self,key,value[0],value[1]))

            self.dense_v_container.body().addWidget(self.demo_dense_v_container)
            self.dense_v_container.body().addPlaceholder(12)
            self.dense_v_container.adjustSize()

            group.addWidget(self.dense_v_container)
        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)



