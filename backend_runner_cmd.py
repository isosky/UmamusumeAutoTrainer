

from bot.base.manifest import register_app, APP_MANIFEST_LIST
from module.umamusume.manifest import UmamusumeManifest
import bot.engine.executor as executor
import bot.base.log as logger


log = logger.get_logger(__name__)


app_name = 'umamusume'
task_execute_mode = 1
task_type = 1
task_desc = '育成'
cron_job_config = None
race_list_caoshangfei = [2401, 3104, 3607, 4409, 5407, 5605, 6807, 7008]
race_list_dahechiji = [1701, 2303, 2703, 2905, 3103, 3303, 3403,
                       4408, 4506, 4608, 4804, 5407, 5605, 6006, 6701, 6807, 7008, 7204]
race_list_shenying = [2303, 2501, 2703, 2905, 3103, 3303, 3404,
                      3601, 4301, 4607, 5201, 5709, 5904, 6006, 6703, 7008, 7204]
expect_attribute_shenying = [1000, 700, 700, 250, 400]
learn_skill_list_shenying = ['圆弧艺术家', '弧线大师', '最后冲刺', '春季优俊少女', '逆时针']
race_list_dashukuaiche = [2303, 2501, 2703, 2905, 3103,
                          3303, 3601, 4301, 4607, 5201, 5709, 5904, 6601, 6703, 7007]
expect_attribute_dashukuaiche = [1100, 600, 700, 250, 400]
learn_skill_list_dashukuaiche = ['弧线大师', '最后冲刺', '春季优俊少女', '逆时针', '专注力']

# 从网页生成 TODO 改成读配置文件 TODO 改成命令行 TODO
attachment_data_dashukuaiche = {'expect_attribute': expect_attribute_dashukuaiche, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_dashukuaiche,
                                'learn_skill_list': learn_skill_list_dashukuaiche, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': False,
                                'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_shenying = {'expect_attribute': expect_attribute_shenying, 'follow_support_card_name': '在耀眼景色的前方', 'follow_support_card_level': 50, 'extra_race_list': race_list_shenying,
                            'learn_skill_list': learn_skill_list_shenying, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': False,
                            'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}

register_app(UmamusumeManifest)
app_config = APP_MANIFEST_LIST[app_name]
task = app_config.build_task(
    task_execute_mode, task_type, task_desc, cron_job_config, attachment_data_shenying)

for k, v in attachment_data_shenying.items():
    log.info(f"{k}:{v}")


task_executor = executor.Executor()
for i in range(3):
    task_executor.start(task)


# if 'factor_list' in task.detail.cultivate_result:
#     if len(task.detail.cultivate_result['factor_list']) > 0:
#         for i in task.detail.cultivate_result['factor_list']:
#             print(i)
