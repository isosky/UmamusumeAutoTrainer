from enum import Enum
from bot.base.task import Task, TaskExecuteMode


class TaskDetail:
    scenario_name: str
    expect_attribute: list[int]
    follow_support_card_name: str
    follow_support_card_level: int
    extra_race_list: list[int]
    learn_skill_list: list[str]
    tactic_list: list[int]
    clock_use_limit: int
    learn_skill_threshold: int
    learn_skill_only_user_provided: bool
    allow_recover_tp: bool
    allow_diamond_recover_tp: bool
    cultivate_progress_info: dict
    extra_weight: list
    prior_support_card_list: list[str]
    black_skill_list: list[str]


class EndTaskReason(Enum):
    TP_NOT_ENOUGH = "训练值不足"


class UmamusumeTask(Task):
    detail: TaskDetail

    def end_task(self, status, reason) -> None:
        super().end_task(status, reason)

    def start_task(self) -> None:
        pass


class UmamusumeTaskType(Enum):
    UMAMUSUME_TASK_TYPE_UNKNOWN = 0
    UMAMUSUME_TASK_TYPE_CULTIVATE = 1


def build_task(task_execute_mode: TaskExecuteMode, task_type: int,
               task_desc: str, cron_job_config: dict, attachment_data: dict) -> UmamusumeTask:
    td = TaskDetail()
    ut = UmamusumeTask(task_execute_mode=task_execute_mode,
                       task_type=UmamusumeTaskType(task_type), task_desc=task_desc, app_name="umamusume")
    ut.cron_job_config = cron_job_config
    td.expect_attribute = attachment_data['expect_attribute']
    td.follow_support_card_level = int(attachment_data['follow_support_card_level'])
    td.follow_support_card_name = attachment_data['follow_support_card_name']
    td.extra_race_list = attachment_data['extra_race_list']
    td.learn_skill_list = attachment_data['learn_skill_list']
    td.tactic_list = attachment_data['tactic_list']
    td.clock_use_limit = attachment_data['clock_use_limit']
    td.learn_skill_threshold = attachment_data['learn_skill_threshold']
    td.learn_skill_only_user_provided = attachment_data['learn_skill_only_user_provided']
    td.allow_recover_tp = attachment_data['allow_recover_tp']
    td.allow_diamond_recover_tp = attachment_data['allow_diamond_recover_tp']
    td.extra_weight = attachment_data['extra_weight']
    td.prior_support_card_list = attachment_data['prior_support_card_list']
    td.black_skill_list = attachment_data['black_skill_list']
    td.cultivate_result = {}
    # td.scenario_name = attachment_data['scenario_name']
    ut.detail = td
    return ut
