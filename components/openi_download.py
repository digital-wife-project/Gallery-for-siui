import subprocess
import re
from PyQt5.QtCore import QThread, pyqtSignal, QObject

class OpeniDownloadWorker(QThread):

    presentage_updated = pyqtSignal(int)
    on_download_finished = pyqtSignal(str)

    def __init__(self, repoid, file, savepath):
        super().__init__()
        print("OpeniDownloadWorker init")
        self.repoid = repoid
        self.file = file
        self.savepath = savepath
        self.running = True
        # 将正则表达式定义移到类级别
        self.regex_percentage = re.compile(r"(\d+)%")

    def run(self):
        filepath = "openi dataset download"
        arguments = f" {self.repoid} {self.file} --cluster NPU --save_path {self.savepath}"
        command = f"{filepath} {arguments}"
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, encoding='utf-8')

        for line in iter(process.stdout.readline, ''):
            if not self.running:
                break
            percentage = self.attackdetail(line)
            if percentage:
                self.presentage_updated.emit(int(percentage))

        process.stdout.close()
        self.on_download_finished.emit(self.file)
        process.wait()

    def attackdetail(self, line):
        match_percentage = self.regex_percentage.search(line)
        percentage = match_percentage.group(1) if match_percentage else None
        return percentage

    def stop(self):
        self.running = False

