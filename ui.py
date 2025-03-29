import icons
from components.page_about import About
from components.page_tools import ExampleContainer
from components.page_setting import ExampleFunctional
from components.page_homepage import ExampleHomepage
from components.page_download import ExampleIcons
from components.page_launch import RefactoredWidgets
from components.page_QA import ExampleWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget

import siui
from siui.core import SiColor, SiGlobal
from siui.templates.application.application import SiliconApplication

# 载入图标
siui.core.globals.SiGlobal.siui.loadIcons(
    icons.IconDictionary(color=SiGlobal.siui.colors.fromToken(SiColor.SVG_NORMAL)).icons
)


class MySiliconApp(SiliconApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        screen_geo = QDesktopWidget().screenGeometry()
        self.setMinimumSize(1024, 380)
        self.resize(1366, 916)
        self.move((screen_geo.width() - self.width()) // 2, (screen_geo.height() - self.height()) // 2)
        self.layerMain().setTitle("Silicon UI Gallery")
        self.setWindowTitle("Silicon UI Gallery")
        self.setWindowIcon(QIcon("./img/empty_icon.png"))

        self.layerMain().addPage(ExampleHomepage(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_home_filled"),
                                 hint="主页", side="top")
        self.layerMain().addPage(ExampleIcons(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_person_voice_regular"),
                                 hint="TTS", side="top")

        self.layerMain().addPage(ExampleIcons(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_textbox_regular"),
                                 hint="LLM", side="top")
        self.layerMain().addPage(ExampleIcons(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_wand_filled"),
                                 hint="SD", side="top")
        self.layerMain().addPage(ExampleIcons(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_scan_person_filled"),
                                 hint="数字人", side="top")
        self.layerMain().addPage(ExampleIcons(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_desktop_arrow_down_filled"),
                                 hint="其他", side="top")

        self.layerMain().addPage(ExampleWidgets(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_question_filled"),
                                 hint="疑难解答", side="top")
        self.layerMain().addPage(ExampleContainer(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_toolbox_regular"),
                                 hint="工具箱", side="top")

        self.layerMain().addPage(About(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_info_filled"),
                                 hint="关于", side="bottom")

        self.layerMain().setPage(0)

        SiGlobal.siui.reloadAllWindowsStyleSheet()

