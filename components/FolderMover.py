import os
import shutil
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressDialog, QVBoxLayout

class FolderMover(QThread):
    progress_updated = pyqtSignal(int)  # Signal to update the progress

    def __init__(self, source, destination):
        super().__init__()
        self.source = source
        self.destination = destination

    def run(self):
        total_files = sum([len(files) for r, d, files in os.walk(self.source)])
        moved_files = 0

        for foldername, subfolders, filenames in os.walk(self.source):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                dest_path = os.path.join(self.destination, os.path.relpath(file_path, self.source))
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.move(file_path, dest_path)
                moved_files += 1
                self.progress_updated.emit(int((moved_files / total_files) * 100))

    # def startMoving(self,source,destination):

    #     self.folderMover = FolderMover(source, destination)
    #     self.folderMover.progress_updated.connect(self.updateProgress)
    #     self.folderMover.start()

    # def updateProgress(self, value):
    #     self.progressDialog.setValue(value)
    #     if value == 100:
    #         self.progressDialog.close()

