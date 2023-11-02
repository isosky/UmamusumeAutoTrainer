from module.umamusume.context import UmamusumeContext
from module.umamusume.define import TurnOperationType


def choose_first_from_two(ctx: UmamusumeContext) -> int:
    return 1


def choose_two_from_two(ctx: UmamusumeContext) -> int:
    return 2


def choose_first_from_three(ctx: UmamusumeContext) -> int:
    return 1


def choose_two_from_three(ctx: UmamusumeContext) -> int:
    return 2


def choose_three_from_three(ctx: UmamusumeContext) -> int:
    return 3


def bbxj_2(ctx: UmamusumeContext) -> int:
    """
    选项1：干劲+1，力量+1，羁绊加5

    选项2：体力+10，羁绊加5

    干劲不到5选1，否则选2
    """
    if ctx.cultivate_detail.turn_info.motivation_level.value < 5:
        return 1
    else:
        return 2


def mccz_1(ctx: UmamusumeContext) -> int:
    """
    选项1：耐力+10，羁绊加5

    选项2：体力+10，耐力+5，羁绊加5

    体力不到50选2，否则选1
    """
    if ctx.cultivate_detail.turn_info.remain_stamina < 50:
        return 2
    else:
        return 1


def tbz_3(ctx: UmamusumeContext) -> int:
    """
    选项1：体力+10，干劲+1，羁绊加5

    选项2：体力-10，耐力+15，pt+15，羁绊加5

    体力不到50并且干劲满选1，否则选2
    """
    if ctx.cultivate_detail.turn_info.remain_stamina < 50 and ctx.cultivate_detail.turn_info.motivation_level.value == 5:
        return 1
    else:
        return 2


def dzyy_2(ctx: UmamusumeContext) -> int:
    """
    第二年6月前都选2，惹人喜爱
    """
    if ctx.cultivate_detail.turn_info.date <= 36:
        return 2
    else:
        return 1
