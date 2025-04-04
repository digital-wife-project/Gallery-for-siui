import os
import shutil
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressDialog, QVBoxLayout

class FolderMover(QThread):
    progress_updated = pyqtSignal(int)  # Signal to update the progress
    finished = pyqtSignal()  # Signal to indicate that the task is finished

    def __init__(self, source, destination):
        super().__init__()
        self.source = source
        self.destination = destination

    def run(self):
        if not os.path.exists(self.source):
            print(f"Source directory {self.source} does not exist.")
            self.finished.emit()
            return

        total_files = sum([len(files) for r, d, files in os.walk(self.source)])
        if total_files == 0:
            print(f"No files to move in {self.source}.")
            self.finished.emit()
            return

        moved_files = 0
        print("Moving files...")
        for foldername, subfolders, filenames in os.walk(self.source):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                dest_path = os.path.join(self.destination, os.path.relpath(file_path, self.source))
                try:
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.move(file_path, dest_path)
                    moved_files += 1
                    self.progress_updated.emit(int((moved_files / total_files) * 100))
                except Exception as e:
                    print(f"Error moving {file_path}: {e}")

        self.finished.emit()
