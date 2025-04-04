from siui.core import GlobalFont, SiColor, SiGlobal
from siui.gui import SiFont
from siui.templates.application.components.message.box import SiSideMessageBox

# ("标准", value=0)
# ("成功", value=1)
# ("提示", value=2)
# ("警告", value=3)
# ("错误", value=4)

def send_simple_message(type_, content,auto_close=False, auto_close_duration=1000):
    fold_after = auto_close_duration if auto_close is True else None
    SiGlobal.siui.windows["MAIN_WINDOW"].LayerRightMessageSidebar().send(
        content,
        msg_type=type_,
        fold_after=fold_after,
    )
