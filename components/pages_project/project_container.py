from PyQt5.QtCore import Qt, pyqtSignal
from siui.components import (
    SiDenseHContainer,
    )
from siui.components.button import (
    SiProgressPushButton,
    SiPushButtonRefactor,
)
from siui.core import SiGlobal

import os
from .project_detail import ChildPage_ProjectDetail
from .model_windows import ModalDownloadDialog
from ..openi_download import OpeniDownloadWorker
from ..launcher import BatRunner
from .DemoLabel import DemoLabel
from ..json_changer import json_changer,loacl_project_json_reader



class Row_for_each_project(SiDenseHContainer):

    on_download_click = pyqtSignal(str,str)

    def __init__(self,parent,project_name,project_detail,file_name):
        self.project_name=project_name
        self.project_detail=project_detail
        self.file_name=file_name

        self.project_path=loacl_project_json_reader(self.project_name)

        super().__init__(parent)
    
        self.demo_progress_button_text = SiProgressPushButton(self)
        
        self.demo_push_button_text = SiPushButtonRefactor(self)
        self.demo_push_button_text.setText("项目管理")

        if self.project_path !=None:
            self.demo_progress_button_text.setText("开始使用")
            self.demo_progress_button_text.setToolTip("点击以开始使用")
            self.demo_progress_button_text.setProgress(100)
            self.demo_progress_button_text.adjustSize()
            self.demo_progress_button_text.clicked.connect(self.launch_click)
            self.demo_push_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerChildPage().setChildPage(ChildPage_ProjectDetail(self,self.project_path)))  # 连接点击信号到槽函数
            self.demo_push_button_text.adjustSize()


        else:
            self.demo_progress_button_text.setText("开始下载")
            self.demo_progress_button_text.setToolTip("点击以开始下载")
            self.demo_progress_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().setDialog(ModalDownloadDialog(self,self.file_name)))
            self.demo_progress_button_text.adjustSize()

        self.addWidget(DemoLabel(self,self.project_name,self.project_detail), "left")
        self.addWidget(self.demo_progress_button_text, "right")
        self.addWidget(self.demo_push_button_text, "right")
        
        self.setAdjustWidgetsSize(True)
        self.addPlaceholder(12)
        self.adjustSize()

        self.on_download_click.connect(self.download_click)

    def download_click(self,file_name,user_path):
        self.downloader(self.project_name,file_name,user_path)

    def launch_click(self):
        self.demo_progress_button_text.setText("正在运行")
        self.launcher = BatRunner(f"{self.project_path}/launch.bat")
        self.launcher.runBatFile()


    def downloader(self,projectname,file_name,user_path):
            self.demo_progress_button_text.setText("正在下载")
            print(f"Download started for file: {user_path}")
            self.download_worker = OpeniDownloadWorker(projectname,"wyyyz/dig",file_name,user_path)
            self.download_worker.presentage_updated.connect(self.presentage_updated)
            self.download_worker.on_download_finished.connect(self.download_finished)
            self.download_worker.finished_unzipping.connect(self.unzipFinished)
            self.download_worker.start()

    def presentage_updated(self, percentage):
        self.demo_progress_button_text.setProgress(percentage/100)
        print(f"Download percentage: {percentage}%")

    def download_finished(self):
        self.demo_progress_button_text.setText("正在解压")

    def unzipFinished(self,project_name,save_path):
        self.demo_progress_button_text.setText("解压完成")
        abs_path = os.path.abspath(save_path)
        print(f"Download finished for file: {abs_path}")
        json_changer(project_name,abs_path)




     