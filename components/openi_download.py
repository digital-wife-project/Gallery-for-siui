import subprocess
import re
from PyQt5.QtCore import QThread, pyqtSignal, QObject

class OpeniDownloadWorker(QThread):
    presentage_updated = pyqtSignal(int)
    size_updated = pyqtSignal(str)
    on_download_finished = pyqtSignal()

    def __init__(self, repoid, file, savepath):
        super().__init__()
        print("OpeniDownloadWorker init")
        self.repoid = repoid
        self.file = file
        self.savepath = savepath
        self.running = True
        # 将正则表达式定义移到类级别
        self.regex_percentage = re.compile(r"(\d+)%")
        self.regex_size = re.compile(r"(\d+M/\d+M)")

    def run(self):
        filepath = "openi dataset download"
        arguments = f" {self.repoid} {self.file} --cluster NPU --save_path {self.savepath}"
        command = f"{filepath} {arguments}"
        print(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, encoding='utf-8')

        for line in iter(process.stdout.readline, ''):
            if not self.running:
                break
            percentage, size = self.attackdetail(line)
            if percentage:
                self.presentage_updated.emit(int(percentage))
            if size:
                self.size_updated.emit(size)

        process.stdout.close()
        self.on_download_finished.emit()
        process.wait()

    def attackdetail(self, line):
        match_percentage = self.regex_percentage.search(line)
        match_size = self.regex_size.search(line)
        percentage = match_percentage.group(1) if match_percentage else None
        size = match_size.group(0) if match_size else None
        return percentage, size

    def stop(self):
        self.running = False

# class OpeniDownload(QObject):

#     presentageupdated = pyqtSignal(int)
#     sizeupdated = pyqtSignal(str)

#     def __init__(self):
#         super().__init__()
#         self.download_worker = None

#     def public_openi_download(self, repoid: str, file: str, savepath: str):
#         self.download_worker = OpeniDownloadWorker(repoid, file, savepath)
#         self.download_worker.presentage_updated.connect(self.on_presentage_updated)
#         self.download_worker.size_updated.connect(self.on_size_updated)
#         self.download_worker.start()

#     def on_presentage_updated(self, percentage):
#         self.presentageupdated.emit(percentage)
#         print(f"Download percentage: {percentage}%")

#     def on_size_updated(self, size):
#         self.sizeupdated.emit(size)
#         print(f"Download size: {size}")

#     def stop_download(self):
#         if self.download_worker and self.download_worker.isRunning():
#             self.download_worker.stop()
#             self.download_worker.wait()

# 在 PyQt 应用中使用 OpeniDownload
# app = QApplication(sys.argv)
# downloader = OpeniDownload()
# downloader.public_openi_download('repoid', 'file', 'savepath')
# app.exec_()
