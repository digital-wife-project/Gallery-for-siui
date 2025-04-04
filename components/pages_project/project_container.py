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
from ..pip_installer import CommandExecutorThread
from .side_message import send_simple_message
from ..json_changer import json_adder,loacl_project_json_reader

class Row_for_each_project(SiDenseHContainer):

    on_download_click = pyqtSignal(str,str)

    def __init__(self,parent,project_name,insatller,project_detail,install_args):
        super().__init__(parent)
        self.project_name=project_name
        self.insatller=insatller
        self.project_detail=project_detail
        self.install_args=install_args

    
        self.demo_progress_button_text = SiProgressPushButton(self)
        self.demo_push_button_text = SiPushButtonRefactor(self)
        self.Refresh()

        self.demo_push_button_text.setText("项目管理")
        self.demo_push_button_text.clicked.connect(lambda:self.Refresh())
        self.demo_push_button_text.adjustSize()

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

    def Refresh(self):
        self.project_path=loacl_project_json_reader(self.project_name)
        if self.project_path !=None:
            self.demo_progress_button_text.setText("开始使用")
            self.demo_progress_button_text.setToolTip("点击以开始使用")
            self.demo_progress_button_text.setProgress(100)
            self.demo_progress_button_text.adjustSize()
            self.demo_progress_button_text.clicked.connect(self.launch_click)
            self.demo_push_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerChildPage().setChildPage(ChildPage_ProjectDetail(self,self.project_name,self.project_path)))  # 连接点击信号到槽函数
            self.demo_push_button_text.adjustSize()
        else:
            self.demo_progress_button_text.setText("开始下载")
            self.demo_progress_button_text.setToolTip("点击以开始下载")
            self.demo_progress_button_text.clicked.connect(lambda: SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().setDialog(ModalDownloadDialog(self,self.install_args)))
            self.demo_progress_button_text.adjustSize()

    def execute_commands(self,commands, working_directory):
        # 定义要执行的命令和路径
        # 创建并启动线程
        self.thread = CommandExecutorThread(commands, working_directory)
        self.thread.output_signal.connect(self.convert_Singnal2Info)
        self.thread.start()

    def convert_Singnal2Info(self,signal_output):
        # 将信号转换为字符串信息
        send_simple_message(0,signal_output,True)

    def downloader(self,projectname,install_arg,user_path):
        self.demo_progress_button_text.setEnabled(False)
        self.demo_progress_button_text.setText("正在下载")
        if self.insatller=="openi":
            self.download_worker = OpeniDownloadWorker(projectname,"wyyyz/dig",install_arg,user_path)
            self.download_worker.presentage_updated.connect(self.presentage_updated)
            self.download_worker.on_download_finished.connect(self.download_finished)
            self.download_worker.finished_unzipping.connect(self.unzipFinished)
            self.download_worker.start()
        if self.insatller=="pip":
            self.execute_commands(install_arg,user_path)


    def presentage_updated(self, percentage):
        self.demo_progress_button_text.setProgress(percentage/100)
        print(f"Download percentage: {percentage}%")

    def download_finished(self):
        self.demo_progress_button_text.setText("正在解压")

    def unzipFinished(self,project_name,save_path):
        self.demo_progress_button_text.setText("解压完成")
        abs_path = os.path.abspath(save_path)
        print(f"Download finished for file: {abs_path}")
        json_adder(project_name,abs_path)
        self.Refresh()
        self.demo_progress_button_text.setEnabled(True)




     