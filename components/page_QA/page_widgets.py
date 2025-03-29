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

from ..option_card import OptionCardPlaneForWidgetDemos
from .components.demo_tables import DemoOsuPlayerRankingTableManager


class ExampleWidgets(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

