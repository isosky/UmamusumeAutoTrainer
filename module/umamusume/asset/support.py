from bot.base.resource import Template
import os
import bot.base.log as logger

log = logger.get_logger(__name__)


UMAMUSUME_UMA_SUPPORTCARD_TEMPLATE_PATH = "resource/umamusume/support_card"
_UMAMUSUME_UMA_SUPPORTCARD_TEMPLATE_PATH = "/umamusume/support_card"
UMA_SUPPORT_CARD_LIST: list[Template] = []


def load_uma_support_card():
    # role
    image_files = [f for f in os.listdir(UMAMUSUME_UMA_SUPPORTCARD_TEMPLATE_PATH) if os.path.isfile(os.path.join(UMAMUSUME_UMA_SUPPORTCARD_TEMPLATE_PATH, f))]
    for i in image_files:
        temp_name = i[:-4]
        temp_name = Template(temp_name, _UMAMUSUME_UMA_SUPPORTCARD_TEMPLATE_PATH)
        UMA_SUPPORT_CARD_LIST.append(temp_name)


load_uma_support_card()
