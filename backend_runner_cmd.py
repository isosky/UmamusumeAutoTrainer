

from bot.base.manifest import register_app, APP_MANIFEST_LIST
from module.umamusume.manifest import UmamusumeManifest
import bot.engine.executor as executor
import bot.base.log as logger
import time

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
# race_list_dashukuaiche = [2303, 2501, 2703, 2905, 3103, 3303, 3601, 4301, 4607, 5201, 5709, 5904, 6601, 6703, 7007]
race_list_dashukuaiche = [2303, 2501, 2703, 3303, 3601, 4301, 4408, 4607, 5201, 5709, 5904, 6006, 6601, 6703, 7007]
expect_attribute_dashukuaiche = [1100, 600, 600, 250, 300]
learn_skill_list_dashukuaiche = ['弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '专注力']


race_list_wanshansiji = [2503, 4202, 4409, 5101, 5605, 6006, 6602, 7008, 7204]
expect_attribute_wanshansiji = [1100, 700, 600, 250, 300]
learn_skill_list_wanshansiji = ['弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '专注力']

race_list_zhongpao = [2303, 2503, 3003, 3104, 3404, 4202, 5101, 5904]
expect_attribute_zhongpao = [1100, 700, 600, 250, 300]
learn_skill_list_zhongpao = ['弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '专注力']


race_list_mubaimaikun = [2203, 2401, 2503, 2903, 3104, 3404, 4804, 5101, 5407, 6602, 7008, 7204]
expect_attribute_mubaimaikun = [1100, 700, 600, 250, 300]
learn_skill_list_mubaimaikun = ['弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '专注力']


# 一颗安心糖
# 在耀眼景色的前方

# 从网页生成 TODO 改成读配置文件 TODO 改成命令行 TODO
attachment_data_dashukuaiche = {'expect_attribute': expect_attribute_dashukuaiche, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_dashukuaiche,
                                'learn_skill_list': learn_skill_list_dashukuaiche, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': True,
                                'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_shenying = {'expect_attribute': expect_attribute_shenying, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_shenying,
                            'learn_skill_list': learn_skill_list_shenying, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': True,
                            'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_wanshansiji = {'expect_attribute': expect_attribute_wanshansiji, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_wanshansiji,
                               'learn_skill_list': learn_skill_list_wanshansiji, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': True,
                               'learn_skill_only_user_provided': False, 'extra_weight': [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_zhongpao = {'expect_attribute': expect_attribute_zhongpao, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_zhongpao,
                            'learn_skill_list': learn_skill_list_zhongpao, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': True,
                            'learn_skill_only_user_provided': False, 'extra_weight': [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}

attachment_data_mubaimaikun = {'expect_attribute': expect_attribute_mubaimaikun, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_mubaimaikun,
                               'learn_skill_list': learn_skill_list_mubaimaikun, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 500, 'allow_recover_tp': True,
                               'learn_skill_only_user_provided': False, 'extra_weight': [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


register_app(UmamusumeManifest)
app_config = APP_MANIFEST_LIST[app_name]
task = app_config.build_task(
    task_execute_mode, task_type, task_desc, cron_job_config, attachment_data_mubaimaikun)

for k, v in attachment_data_mubaimaikun.items():
    log.info(f"{k}:{v}")


task_executor = executor.Executor()
for i in range(10):
    task_executor.start(task)
    time.sleep(2)
