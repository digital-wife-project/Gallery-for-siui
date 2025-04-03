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
    SiOptionCardPlane,
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
from siui.components.page.child_page import SiChildPage

from siui.core import Si, SiColor, SiGlobal,GlobalFont
from siui.gui import SiFont

from ..project_detail import ChildPage_ProjectDetail
from ..model_windows import ModalDownloadDialog
from ...openi_download import OpeniDownloadWorker
from ...unziper import UnzipThread
from ... option_card import OptionCardPlaneForWidgetDemos
from ..project_container import rowofeachproject

import datetime
import random
import threading
import time
import json


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
            self.demo_dense_v_container.addWidget(rowofeachproject(self,"bert","tgfhtrh","game.zip","ttttdtfhgf"))

            self.dense_v_container.body().addWidget(self.demo_dense_v_container)
            self.dense_v_container.body().addPlaceholder(12)
            self.dense_v_container.adjustSize()

            group.addWidget(self.dense_v_container)
        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)

    def save_config(name,path,bat):
    #设置./config/projects/{name}.json中的文件的内容
        with open(f'./config/projects/{name}.json', 'w') as f:
            json.dump({"path": path, "bat": bat}, f)
        pass



