from PyQt5.QtCore import Qt,QPointF, QRectF,QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QVBoxLayout

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
    SiWidget,
    )
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

from siui.core import Si, SiColor, SiGlobal,GlobalFont
from siui.gui import SiFont

import sys
from ..model_windows import ModalDownloadDialog
from ...openi_download import OpeniDownloadWorker
from ...unziper import UnzipThread
from ... option_card import OptionCardPlaneForWidgetDemos

import datetime
import random
import schedule
import threading
import time

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
#################################################################################################################################################################################
            container = SiDenseHContainer(self)

            self.demo_progress_button_text = SiProgressPushButton(self)
            self.demo_progress_button_text.setText("启动")
            self.demo_progress_button_text.setToolTip("点击以开始下载或使用")
            self.demo_progress_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().setDialog(ModalDownloadDialog(self,"game.zip")))
            
            self.demo_progress_button_text.adjustSize()

            self.demo_push_button_text = SiPushButtonRefactor(self)
            self.demo_push_button_text.setText("项目管理")
            self.demo_push_button_text.clicked.connect(self.download_bert_button_clicked)  # 连接点击信号到槽函数
            self.demo_push_button_text.adjustSize()

            container.addWidget(DemoLabel(self,"bert","使用 setHint 方法设置工具提示"), "left")
            container.addWidget(self.demo_progress_button_text, "right")
            container.addWidget(self.demo_push_button_text, "right")

            container.setAdjustWidgetsSize(True)
            container.addPlaceholder(12)
            container.adjustSize()
###########################################################################################################################################################################
            self.demo_dense_v_container.addWidget(container)

            self.dense_v_container.body().addWidget(self.demo_dense_v_container)
            self.dense_v_container.body().addPlaceholder(12)
            self.dense_v_container.adjustSize()

            group.addWidget(self.dense_v_container)
        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)

    def download_bert_button_clicked(self):
        if self.message_type == 0:
            print("下载")
            self.demo_progress_button_text.setText("正在下载")
            self.download_worker = OpeniDownloadWorker("bert","wyyyz/dig","game.zip","./tmp")
            self.download_worker.presentage_updated.connect(self.on_presentage_updated)
            self.download_worker.on_download_finished.connect(self.download_finished)
            self.download_worker.start()

    def on_presentage_updated(self, percentage):
        self.demo_progress_button_text.setProgress(percentage/100)
        print(f"Download percentage: {percentage}%")

    def download_finished(self,filename,project_name):
        self.demo_progress_button_text.setText("正在解压")
        self.unzip(filename,project_name)

    def unzip(self,filename,project_name):
        self.unzipThread = UnzipThread(f'./tmp/{filename}','./project',project_name)
        self.unzipThread.progress.connect(self.on_presentage_updated)
        self.unzipThread.finished_unzipping.connect(self.unzipFinished)
        self.unzipThread.start()

    def unzipFinished(self):
        self.demo_progress_button_text.setText("解压完成")



