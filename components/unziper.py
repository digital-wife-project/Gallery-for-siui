import sys
import zipfile
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton, QLabel


class UnzipThread(QThread):
    # 创建一个信号，用于更新进度条
    progress = pyqtSignal(int)
    # 创建一个信号，用于表示解压完成
    finished_unzipping = pyqtSignal(str)

    def __init__(self, zip_file_path, extract_path,project_name):
        super().__init__()
        self.project_name=project_name
        self.zip_file_path = zip_file_path
        self.extract_path = extract_path

    def run(self):
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            # 获取ZIP文件中所有文件的总大小
            total_size = sum((file_info.file_size for file_info in zip_ref.infolist()))
            extracted_size = 0

            # 遍历ZIP文件中的所有文件
            for file_info in zip_ref.infolist():
                # 解压单个文件
                zip_ref.extract(file_info, self.extract_path)
                # 更新已解压的大小
                extracted_size += file_info.file_size
                # 发送信号以更新进度条
                self.progress.emit(int((extracted_size / total_size) * 100))

            # 发送信号表示解压完成

            self.finished_unzipping.emit(self.project_name)
