from siui.components import SiLabel, SiLongPressButton, SiPushButton
from siui.core import SiColor, SiGlobal
from siui.templates.application.components.dialog.modal import SiModalDialog


class ModalDownloadDialog(SiModalDialog):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedWidth(500)
        self.icon().load(SiGlobal.siui.iconpack.get("ic_fluent_save_filled",
                                                    color_code=SiColor.mix(
                                                        self.getColor(SiColor.SVG_NORMAL),
                                                        self.getColor(SiColor.INTERFACE_BG_B),
                                                        0.05))
                         )

        label = SiLabel(self)
        label.setStyleSheet(f"color: {self.getColor(SiColor.TEXT_E)}")
        label.setText(
            f'<span style="color: {self.getColor(SiColor.TEXT_B)}">选择项目的安装位置</span><br>'
        )
        label.adjustSize()
        self.contentContainer().addWidget(label)

        button1 = SiPushButton(self)
        button1.setFixedHeight(32)
        button1.attachment().setText("使用默认位置")
        button1.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button1.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        button2 = SiPushButton(self)
        button2.setFixedHeight(32)
        button2.attachment().setText("自定义安装位置")
        button2.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button2.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        self.button3 = SiLongPressButton(self)
        self.button3.setFixedHeight(32)
        self.button3.attachment().setText("开始下载与安装")
        self.button3.longPressed.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)

        button4 = SiPushButton(self)
        button4.setFixedHeight(32)
        button4.attachment().setText("取消")
        button4.colorGroup().assign(SiColor.BUTTON_PANEL, self.getColor(SiColor.INTERFACE_BG_D))
        button4.clicked.connect(SiGlobal.siui.windows["MAIN_WINDOW"].layerModalDialog().closeLayer)


        self.buttonContainer().addWidget(button1)
        self.buttonContainer().addWidget(button2)
        self.buttonContainer().addWidget(self.button3)
        self.buttonContainer().addWidget(button4)

        SiGlobal.siui.reloadStyleSheetRecursively(self)
        self.adjustSize()

