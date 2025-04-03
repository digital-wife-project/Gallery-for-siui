from os import name
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

from .project_detail import ChildPage_ProjectDetail
from .model_windows import ModalDownloadDialog
from ..openi_download import OpeniDownloadWorker
from ..unziper import UnzipThread
from .. option_card import OptionCardPlaneForWidgetDemos

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



class rowofeachproject(SiDenseHContainer):
    def __init__(self,parent,project_name,project_detail,file_name,launch_command):
        self.project_name=project_detail
        self.project_detail=project_detail
        self.file_name=file_name
        self.launch_command=launch_command
        super().__init__(parent)
    
        self.demo_progress_button_text = SiProgressPushButton(self)
        self.demo_progress_button_text.setText("启动")
        self.demo_progress_button_text.setToolTip("点击以开始下载或使用")
        self.demo_progress_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().setDialog(ModalDownloadDialog(self,self.file_name)))
        
        
        self.demo_progress_button_text.adjustSize()
        
        self.demo_push_button_text = SiPushButtonRefactor(self)
        self.demo_push_button_text.setText("项目管理")
        self.demo_push_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerChildPage().setChildPage(ChildPage_ProjectDetail(self)))  # 连接点击信号到槽函数
        self.demo_push_button_text.adjustSize()
        
        self.addWidget(DemoLabel(self,self.project_name                                                                                         ,self.project_detail), "left")
        self.addWidget(self.demo_progress_button_text, "right")
        self.addWidget(self.demo_push_button_text, "right")
        
        self.setAdjustWidgetsSize(True)
        self.addPlaceholder(12)
        self.adjustSize()

    def download_bert_button_clicked(self,file_name):
        if self.message_type == 0:
            print("下载")
            self.demo_progress_button_text.setText("正在下载")
            self.download_worker = OpeniDownloadWorker(file_name,"wyyyz/dig","game.zip","./tmp")
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



     