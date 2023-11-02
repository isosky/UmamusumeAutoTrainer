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
    "相互扶持的秘诀": choose_first_from_three,  # 通用 1：10速
    "用回忆中的美味嗨起来☆": tilipanduan,  # 通用 1：10体力，2：30体力，长胖
    "媲美训练员的知识储备": choose_first_from_two,  # 记者 1：10力量，2：10速

    "怎么办": choose_two_from_two,  # 无声铃鹿-逆时针

    "好心总会有好报": choose_first_from_two,  # 北黑
    "啊，友情": bbxj_2,  # 北黑

    "于夜晚独自奔跑": mccz_1,  # 曼城茶座
    "喜好静谧": choose_first_from_two,  # 曼城茶座

    "舞蹈课": choose_two_from_two,  # 大和赤骥 1：毅力+10,2:速度+10
    "那家伙的存在": choose_two_from_two,  # 大和赤骥-跑日本德比

    "这也烦恼，那也烦恼！": tbz_3,  # 速度-特别周选项

    "贴心关怀也包在我身上人": choose_two_from_two,  # 小海湾

    "一起做料理吧！": choose_first_from_two,  # 丸善斯基，1给10速
    "街上的流行制造者人": choose_first_from_two,  # 丸善斯基 1：10速10智，2：20力
    "沉迷跳舞！": choose_first_from_two,  # 丸善斯基 1：10速，2：10力
    "嘿小姑娘，一起来玩啊": choose_first_from_two,  # 丸善斯基 1：10体力
    "家务技能也不在话下！": choose_two_from_two,  # 丸善斯基 2：10耐10力

    "绝妙☆错误！": dzyy_2,
    "好朋友？": choose_first_from_two,  # 东周  2是孤狼
    "恶作剧也要有计划": choose_first_from_two,  # 东周  2是孤狼

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
