import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from ui import MySiliconApp

import siui
from siui.core import SiGlobal

import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def restart_as_admin():
    if not is_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def show_version_message(window):
    window.LayerRightMessageSidebar().send(
        title="Welcome to Silicon UI Gallery",
        text="You are currently running v1.14.514\n"
             "Click this message box to check out what's new.",
        msg_type=1,
        icon=SiGlobal.siui.iconpack.get("ic_fluent_hand_wave_filled"),
        fold_after=5000,
        slot=lambda: window.LayerRightMessageSidebar().send("Oops, it seems that nothing will happen due to the fact "
                                                            "that this function is currently not completed.",
                                                            icon=SiGlobal.siui.iconpack.get("ic_fluent_info_regular"))
    )

    window.LayerRightMessageSidebar().send(
        title="Refactoring in Progress",
        text="To optimize the project structure, "
             "we are currently undergoing a refactoring process.\n\n"
             "We strongly discourage you from using any deprecated components "
             'other than those displayed on the "Refactored Components" page.',
        msg_type=4,
        icon=SiGlobal.siui.iconpack.get("ic_fluent_warning_filled"),
    )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # if not is_admin():
    #     restart_as_admin()
    #     sys.exit(0)  # Exit the current instance


    window = MySiliconApp()
    window.show()

    timer = QTimer(window)
    timer.singleShot(500, lambda: show_version_message(window))

    sys.exit(app.exec_())
