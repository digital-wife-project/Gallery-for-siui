import asyncio
import datetime
import random

import numpy
from PyQt5.QtCore import QPointF, QRectF, Qt
from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QGraphicsBlurEffect, QLabel

from siui.components import (
    SiCircularProgressBar,
    SiDenseVContainer,
    SiLineEditWithDeletionButton,
    SiLineEditWithItemName,
    SiOptionCardLinear,
    SiTitledWidgetGroup,
    SiWidget,
)
from siui.components.button import (
    SiFlatButton,
    SiLongPressButtonRefactor,
    SiProgressPushButton,
    SiPushButtonRefactor,
    SiRadioButtonRefactor,
    SiRadioButtonWithAvatar,
    SiRadioButtonWithDescription,
    SiSwitchRefactor,
    SiToggleButtonRefactor,
)
from siui.components.chart import SiTrendChart
from siui.components.combobox import SiComboBox
from siui.components.editbox import SiLineEdit
from siui.components.label import HyperRoundBorderTest
from siui.components.menu import SiMenu
from siui.components.page import SiPage
from siui.components.progress_bar import SiProgressBar
from siui.components.slider import SiSliderH
from siui.components.slider_ import SiCoordinatePicker2D, SiCoordinatePicker3D, SiSlider
from siui.components.spinbox.spinbox import SiDoubleSpinBox, SiIntSpinBox
from siui.components.widgets import (
    SiCheckBox,
    SiDenseHContainer,
    SiDraggableLabel,
    SiIconLabel,
    SiLabel,
    SiLongPressButton,
    SiPixLabel,
    SiPushButton,
    SiRadioButton,
    SiSimpleButton,
    SiSwitch,
    SiToggleButton,
)
from siui.components.widgets.expands import SiHoverExpandWidget
from siui.components.widgets.navigation_bar import SiNavigationBarH, SiNavigationBarV
from siui.components.widgets.table import SiTableView
from siui.components.widgets.timedate import SiCalenderView, SiTimePicker, SiTimeSpanPicker
from siui.components.widgets.timeline import SiTimeLine, SiTimeLineItem
from siui.core import Si, SiColor, SiGlobal

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import sys
from ...openi_download import OpeniDownloadWorker

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
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

import random
import schedule
import threading
import time

from siui.components import (
    SiCircularProgressBar,
    SiLineEditWithItemName,
    SiOptionCardLinear,
    SiOptionCardPlane,
    SiPushButton,
    SiTitledWidgetGroup,
)
from siui.components.page.child_page import SiChildPage
from siui.core import SiGlobal
import json

def save_config(name,path,bat):
    #设置./config/projects/{name}.json中的文件的内容
    with open(f'./config/projects/{name}.json', 'w') as f:
        json.dump({"path": path, "bat": bat}, f)
    pass

class TTS(SiPage):
    def __init__(self, *args, **kwargs):
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
            self.dense_v_container.setTitle("竖直密堆积容器")

            self.demo_dense_v_container = SiDenseVContainer(self)
            self.demo_dense_v_container.setFixedHeight(300)
            self.push_buttons = OptionCardPlaneForWidgetDemos(self)

            container = SiDenseHContainer(self)

            self.demo_progress_button_text = SiProgressPushButton(self)
            self.demo_progress_button_text.setText("启动")
            self.demo_progress_button_text.setToolTip("点击以开始下载或使用")
            self.demo_progress_button_text.clicked.connect(self.download_button_clicked)
            

            self.demo_progress_button_text.adjustSize()

            self.demo_push_button_text = SiPushButtonRefactor(self)
            self.demo_push_button_text.setText("项目管理")
            self.demo_push_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerChildPage().setChildPage(ChildPageExample2(self)))  # 连接点击信号到槽函数
            self.demo_push_button_text.adjustSize()

            self.demo_label_hinted = SiLabel(self)
            self.demo_label_hinted.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.demo_label_hinted.setText("Bert-VITS2                                                                                         ")
            self.demo_label_hinted.setHint("一个开源的语音合成项目")

            self.demo_label = SiLabel(self)
            self.demo_label.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.demo_label.setText("               ")

            container.addWidget(self.demo_label, "right")
            container.addWidget(self.demo_progress_button_text, "right")
            container.addWidget(self.demo_push_button_text, "right")

            container.addWidget(self.demo_label_hinted, "left")

            self.demo_dense_v_container.addWidget(container)

            self.dense_v_container.body().addWidget(self.demo_dense_v_container)
            self.dense_v_container.body().addPlaceholder(12)
            self.dense_v_container.adjustSize()

            group.addWidget(self.dense_v_container)
        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)

    def download_button_clicked(self):
        if self.message_type == 0:
            print("下载")
            self.demo_progress_button_text.setText("正在下载")
            self.download_worker = OpeniDownloadWorker("wyyyz/dig","HiyoriUI-0.8.0.zip","./temp")
            self.download_worker.presentage_updated.connect(self.on_presentage_updated)
            self.download_worker.size_updated.connect(self.on_size_updated)
            self.download_worker.on_download_finished.connect(self.finished)
            self.download_worker.start()

    def on_presentage_updated(self, percentage):
        self.demo_progress_button_text.setProgress(percentage/100)
        print(f"Download percentage: {percentage}%")

    def on_size_updated(self, size):
        print(f"Download size: {size}")

    def finished(self):
        self.demo_progress_button_text.setText("启动")

class ChildPageExample2(SiChildPage):
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

            self.line_edit_description = SiLineEditWithItemName(self)
            self.line_edit_description.setName("项目启动bat")
            self.line_edit_description.setFixedHeight(32)

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