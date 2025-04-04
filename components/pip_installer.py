from PyQt5.QtCore import QThread, QProcess, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton

class CommandExecutorThread(QThread):
    # 定义一个信号，用于将输出传递回主线程
    output_signal = pyqtSignal(str)

    def __init__(self, commands, working_directory, parent=None):
        super(CommandExecutorThread, self).__init__(parent)
        self.commands = commands
        self.working_directory = working_directory

    def run(self):
        for command in self.commands:
            process = QProcess()
            process.setWorkingDirectory(self.working_directory)
            process.start(command)

            # 等待进程结束
            process.waitForFinished(-1)  # -1 表示无限等待

            # 读取输出
            output = process.readAllStandardOutput().data().decode()
            error = process.readAllStandardError().data().decode()

            # 发送信号，将输出传递回主线程
            self.output_signal.emit(output)
            if error:
                self.output_signal.emit(error)

            # 确保进程被正确释放
            process.close()
