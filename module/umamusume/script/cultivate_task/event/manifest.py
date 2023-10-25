from typing import Union

from bot.recog.ocr import find_similar_text
from module.umamusume.context import UmamusumeContext
from module.umamusume.script.cultivate_task.event.scenario_event import scenario_event_1, scenario_event_2
from module.umamusume.script.cultivate_task.event.support_card_event import *
import bot.base.log as logger

log = logger.get_logger(__name__)

event_map: dict[str, Union[callable, int]] = {
    "安心～针灸师，登☆场": 5,
    "新年的抱负": scenario_event_1,
    "新年参拜": scenario_event_2,
    "新年祈福": scenario_event_2,
    "追加的自主训练": choose_two_from_two,
    "怎么办": choose_two_from_two,  # 无声铃鹿-逆时针
    "那家伙的存在": choose_two_from_two,  # 大和赤骥-跑日本德比
    "啊，友情": bbxj_2,
    "于夜晚独自奔跑": mccz_1,
    "喜好静谧": choose_first_from_two,
    "舞蹈课": choose_two_from_two,  # 大和赤骥 1：毅力+10,2:速度+10
    "这也烦恼，那也烦恼！": tbz_3,  # 特别周选项
    "媲美训练员的知识储备": choose_first_from_two  # 记者 1：10力量，2：10速
}

event_name_list: list[str] = [*event_map]


def get_event_choice(ctx: UmamusumeContext, event_name: str) -> int:
    event_name_normalized = find_similar_text(event_name, event_name_list, 0.8)
    if event_name_normalized != "":
        if event_name_normalized in event_map:
            opt = event_map[event_name_normalized]
            if type(opt) is int:
                log.info(">>>>> %s 选择 %d", event_name, opt)
                return opt
            if callable(opt):
                return opt(ctx)
            else:
                log.warning("事件[%s]未提供处理逻辑", event_name_normalized)
                return 1
    log.error(f"{event_name} 有选项没默认值")
    log.debug("未知事件[%s]，使用默认选项1", event_name)
    return 1
