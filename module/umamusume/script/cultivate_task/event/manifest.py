from typing import Union

from bot.recog.ocr import find_similar_text
from module.umamusume.context import UmamusumeContext
from module.umamusume.script.cultivate_task.event.scenario_event import scenario_event_1, scenario_event_2
from module.umamusume.script.cultivate_task.event.support_card_event import *
import bot.base.log as logger

log = logger.get_logger(__name__)

event_map: dict[str, Union[callable, int]] = {
    "安心～针灸师，登☆场": 4,  # 赌爱娇
    "新年的抱负": scenario_event_1,
    "新年参拜": scenario_event_2,
    "新年祈福": scenario_event_2,
    "追加的自主训练": choose_second_from_two,
    "相互扶持的秘诀": choose_first_from_three,  # 通用 1：10速
    "用回忆中的美味嗨起来☆": tilipanduan,  # 通用 1：10体，2：30体，长胖
    "媲美训练员的知识储备": choose_first_from_two,  # 记者 1：10力，2：10速
    "愉快！贴身采访！": choose_first_from_two,  # 记者 1：10耐，2：10毅
    "比赛胜利！": choose_first_from_two,  # 通用
    "赛事入围": choose_first_from_two,  # 通用
    "比赛落败": choose_first_from_two,
    "夏季集训（第2年）期间": choose_first_from_two,  # 通用
    "夏季集训（第3年）结束": choose_first_from_two,  # 通用

    "怎么办": choose_second_from_two,  # 无声铃鹿-逆时针

    "好心总会有好报": choose_first_from_two,  # 北黑
    "啊，友情": bbxj_2,  # 北黑

    "于夜晚独自奔跑": mccz_1,  # 曼城茶座
    "喜好静谧": choose_first_from_two,  # 曼城茶座

    "舞蹈课": choose_second_from_two,  # 大和赤骥 1：毅+10,2:速+10
    "那家伙的存在": choose_second_from_two,  # 大和赤骥-跑日本德比

    "这也烦恼，那也烦恼！": tbz_3,  # 速-特别周选项

    "贴心关怀也包在我身上人": choose_second_from_two,  # 小海湾

    "一起做料理吧！": choose_first_from_two,  # 丸善斯基，1给10速
    "街上的流行制造者人": choose_first_from_two,  # 丸善斯基 1：10速10智，2：20力
    "沉迷跳舞！": choose_first_from_two,  # 丸善斯基 1：10速，2：10力
    "嘿小姑娘，一起来玩啊": choose_first_from_two,  # 丸善斯基 1：10体
    "家务技能也不在话下！": choose_second_from_two,  # 丸善斯基 2：10耐10力

    "绝妙☆错误！": dzyy_2,
    "好朋友？": choose_first_from_two,  # 东周  2是孤狼
    "恶作剧也要有计划": choose_first_from_two,  # 东周  2是孤狼

    "黄金船式约会": choose_first_from_two,  # 黄金船 1：20耐，2：20力
    "吃撑勿论！": choose_second_from_two,  # 黄金船2：30体，可能长胖
    "主角的红色！": choose_first_from_two,  # 黄金船 1：20智，2：20毅
    "黄金船！突然讲述过去篇！": choose_first_from_two,  # 黄金船 1：10智10耐,2：20速
    "多人折扣的惯犯": choose_second_from_two,  # 黄金船 1：10毅，2：10耐
    "第二天双双哑了嗓子": choose_first_from_two,  # 黄金船 1：10耐，2：10毅
    "呢，我打的工很不妙吗？": choose_first_from_two,  # 黄金船 1：10耐15pt，2：阪神赛场
    "遗失的物品是？": choose_first_from_two,  # 黄金船 1：20力-10体，2：10速
    "宝家纪念赛后：关键词②": choose_first_from_two,  # 黄金船
    "来吧，一决胜负！": choose_first_from_two,  # 黄金船
    "在夜晚的公园玩要吧": choose_second_from_two,  # 黄金船 1：10毅，2：10速
    "在夜晚的公园玩耍吧": choose_second_from_two,  # 黄金船 1：10毅，2：10速


    "学会绝招吧！": choose_second_from_two,  # 微光飞驹 2：30耐
    "英雄的烦恼": choose_first_from_two,  # 微光飞驹 1：15体，2：5体，5力

    "赐予你提议的权利！": choose_first_from_two,  # 帝王光辉 1：10毅5智
    "赐予你陪我的权利！": choose_first_from_two,  # 帝王光辉

    "想说声谢谢！": choose_first_from_two,  # 力西野花 1：5力，2：5智
    "温馨的爱心便当": choose_first_from_two,  # 力西野花 1：爱娇

    "帮忙也包在我身上": cjxl_1,  # 超级溪流 1：15体力，2：10耐


    "奔跑不息": choose_first_from_two,  # 无声铃鹿 1：10速5耐，2：15速
    "怎么办": choose_second_from_two,  # 无声铃鹿 1：5速耐力，2：逆时针


    "读书少女和魔法少女？": choose_second_from_two,  # 荒漠英雄

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
    log.critical(f"{event_name} 有选项没默认值")
    log.debug("未知事件[%s]，使用默认选项1", event_name)
    return 1
