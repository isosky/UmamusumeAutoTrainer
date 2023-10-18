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


def bbxj_ayq(ctx: UmamusumeContext) -> int:
    """
    选项1：干劲+1，力量+1，羁绊加5

    选项2：体力+10，羁绊加5

    干劲不到5选1，否则选2
    """
    if ctx.cultivate_detail.turn_info.motivation_level.value < 5:
        return 1
    else:
        return 2
