import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import QObject, QProcess

class BatRunner(QObject):
    def __init__(self, bat_file_path):
        super().__init__()
        self.bat_file_path = bat_file_path

        # 创建QProcess对象
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.readOutput)
        self.process.readyReadStandardError.connect(self.readErrors)

    def runBatFile(self):
        # 设置工作目录到.bat文件所在的目录
        bat_directory = os.path.dirname(self.bat_file_path)
        self.process.setWorkingDirectory(bat_directory)

        # 运行.bat文件
        self.process.start(self.bat_file_path)

    def readOutput(self):
        # 读取标准输出
        output = self.process.readAllStandardOutput().data().decode('utf-8', errors='replace')
        print(output)

    def readErrors(self):
        # 读取标准错误输
        errors = self.process.readAllStandardError().data().decode('utf-8', errors='replace')
        print(errors)

