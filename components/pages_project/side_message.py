from siui.core import GlobalFont, SiColor, SiGlobal
from siui.gui import SiFont
from siui.templates.application.components.message.box import SiSideMessageBox


def send_simple_message(type_, auto_close=False, auto_close_duration=1000):
    fold_after = auto_close_duration if auto_close is True else None
    SiGlobal.siui.windows["MAIN_WINDOW"].LayerRightMessageSidebar().send(
        "这是一条测试消息\n"
        "比具标题信息更加简洁方便",
        msg_type=type_,
        fold_after=fold_after,
    )
