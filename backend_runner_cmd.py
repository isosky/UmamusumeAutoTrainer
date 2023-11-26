

from bot.base.manifest import register_app, APP_MANIFEST_LIST
from module.umamusume.manifest import UmamusumeManifest
import bot.engine.executor as executor
import bot.base.log as logger
import time
import copy

log = logger.get_logger(__name__)


app_name = 'umamusume'
task_execute_mode = 1
task_type = 1

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
learn_skill_list_dashukuaiche = ['圆弧艺术家', '弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针']


race_list_wanshansiji = [2203, 2503, 4202, 4409, 5101, 5605, 6006, 6602, 7008, 7204]
expect_attribute_wanshansiji = [1100, 800, 600, 200, 300]
learn_skill_list_wanshansiji = ['圆弧艺术家', '弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '胜利射击！', '弯道能手', '长距离弯道', '标准距离', '中距离直线', '中距离弯道', '良场地']

race_list_zhongpao = [2203, 2401, 2503, 2903, 3104, 3404, 4202, 5101, 6602, 7008]
expect_attribute_zhongpao = [1100, 800, 600, 150, 250]
learn_skill_list_zhongpao = ['圆弧艺术家', '弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '胜利射击！', '弯道能手', '长距离弯道', '标准距离', '中距离直线', '中距离弯道', '良场地']


race_list_mubaimaikun = [2203, 2401, 2503, 2903, 3404, 4804, 5101, 5407, 6602, 7008, 7204]
expect_attribute_mubaimaikun = [1100, 700, 600, 150, 300]
learn_skill_list_mubaimaikun = ['圆弧艺术家', '弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '胜利射击！', '弯道能手', '长距离弯道', '标准距离', '中距离直线', '中距离弯道', '良场地']


race_list_mubailaien = [2203, 2401, 2903, 4202, 5101, 5407, 5605, 6602, 6807, 7008]
expect_attribute_mubailaien = [1100, 800, 600, 150, 300]
learn_skill_list_mubailaien = ['圆弧艺术家', '弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '胜利射击！', '弯道能手', '长距离弯道', '标准距离', '中距离直线', '中距离弯道', '良场地']


race_list_huangjinchuan = [3404, 3607, 4608, 5801]
expect_attribute_huangjinchuan = [1150, 800, 1050, 100, 200]
learn_skill_list_huangjinchuan = ['圆弧艺术家', '弧线大师', '东京赛场', '最后冲刺', '春季优俊少女', '逆时针', '胜利射击！', '弯道能手', '长距离弯道', '标准距离', '中距离直线', '中距离弯道', '良场地']


race_list_donghaidiwang = [2203, 2401, 3304, 3607, 4506, 4804, 6807]
expect_attribute_donghaidiwang = [750, 900, 800, 100, 200]
learn_skill_list_donghaidiwang = ['比赛策略家', '圆弧艺术家', '东京赛场', '标准距离',  '良场地', '春季优俊少女', '顺时针',
                                  '大胃储备', '深呼吸', '吞噬体力', '放学后的乐趣', '后方待机',
                                  '弯道能手', '长距离弯道',  '长距离直线',  '后追直线',
                                  '一鼓作气', '打基础']

race_list_tebiezhou = [2203, 2401, 3304, 3607, 4506, 4804, 6807]
expect_attribute_tebiezhou = [800, 900, 800, 100, 200]
learn_skill_list_tebiezhou = ['比赛策略家', '圆弧艺术家', '东京赛场', '标准距离',  '良场地', '春季优俊少女', '顺时针',
                              '大胃储备', '深呼吸', '吞噬体力', '放学后的乐趣', '后方待机',
                              '弯道能手', '长距离弯道',  '长距离直线',  '后追直线',
                              '一鼓作气', '打基础']


# 一颗安心糖
# 在耀眼景色的前方

# 从网页生成 TODO 改成读配置文件 TODO 改成命令行 TODO
attachment_data_dashukuaiche = {'expect_attribute': expect_attribute_dashukuaiche, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_dashukuaiche,
                                'learn_skill_list': learn_skill_list_dashukuaiche, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 700, 'allow_recover_tp': False, 'allow_diamond_recover_tp': True,
                                'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_shenying = {'expect_attribute': expect_attribute_shenying, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_shenying,
                            'learn_skill_list': learn_skill_list_shenying, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 700, 'allow_recover_tp': False, 'allow_diamond_recover_tp': True,
                            'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_wanshansiji = {'expect_attribute': expect_attribute_wanshansiji, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_wanshansiji,
                               'learn_skill_list': learn_skill_list_wanshansiji, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 700, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True,
                               'learn_skill_only_user_provided': False, 'extra_weight': [[1, 1, 0, 0, 0], [0.5, 1, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_zhongpao = {'expect_attribute': expect_attribute_zhongpao, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_zhongpao,
                            'learn_skill_list': learn_skill_list_zhongpao, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 700, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True,
                            'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}

attachment_data_mubaimaikun = {'expect_attribute': expect_attribute_mubaimaikun, 'follow_support_card_name': '一颗安心糖', 'follow_support_card_level': 50, 'extra_race_list': race_list_mubaimaikun,
                               'learn_skill_list': learn_skill_list_mubaimaikun, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 700, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True,
                               'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_mubailaien = {'expect_attribute': expect_attribute_mubailaien, 'follow_support_card_name': '在耀眼景色的前方', 'follow_support_card_level': 50, 'extra_race_list': race_list_mubailaien,
                              'learn_skill_list': learn_skill_list_mubailaien, 'tactic_list': [4, 4, 4], 'clock_use_limit': 3, 'learn_skill_threshold': 700, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True,
                              'learn_skill_only_user_provided': False, 'extra_weight': [[0.7, 1, 0, 0, 0], [0.7, 1, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_huangjinchuan = {'expect_attribute': expect_attribute_huangjinchuan, 'follow_support_card_name': '必杀技！双胡萝卜拳！', 'follow_support_card_level': 50, 'extra_race_list': race_list_huangjinchuan,
                                 'learn_skill_list': learn_skill_list_huangjinchuan, 'tactic_list': [1, 1, 1], 'clock_use_limit': 3, 'learn_skill_threshold': 2000, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True,
                                 'learn_skill_only_user_provided': False, 'extra_weight': [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]}


attachment_data_donghaidiwang = {'uma_name': '东海帝王', 'expect_attribute': expect_attribute_donghaidiwang, 'follow_support_card_name': '不沉舰的进击', 'follow_support_card_level': 50, 'extra_race_list': race_list_donghaidiwang,
                                 'learn_skill_list': learn_skill_list_donghaidiwang, 'tactic_list': [3, 3, 3], 'clock_use_limit': 1, 'learn_skill_threshold': 800, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True,
                                 'learn_skill_only_user_provided': True, 'extra_weight': [[0.5, 1, 0, 0, 0], [0, 0.5, 0, 0, 0], [0, 0, 0, 0, 0]]}

attachment_data_tebiezhou = {'uma_name': '特别周', 'expect_attribute': expect_attribute_tebiezhou, 'follow_support_card_name': '不沉舰的进击', 'follow_support_card_level': 50,
                             'extra_race_list': race_list_tebiezhou, 'learn_skill_list': learn_skill_list_tebiezhou, 'tactic_list': [3, 3, 3], 'clock_use_limit': 1,
                             'learn_skill_threshold': 800, 'allow_recover_tp': True, 'allow_diamond_recover_tp': True, 'learn_skill_only_user_provided': True,
                             'extra_weight': [[0.5, 1, 0, 0, 0], [0, 0.5, 0, 0, 0], [0, 0, 0, 0, 0]]}


register_app(UmamusumeManifest)
app_config = APP_MANIFEST_LIST[app_name]

task_desc = '种马'


task_executor = executor.Executor()
for i in range(20):
    _attachmet = copy.deepcopy(attachment_data_tebiezhou)
    log.error("**********    新的一盘")
    for k, v in _attachmet.items():
        log.error(f"{k}:{v}")
    task = app_config.build_task(
        task_execute_mode, task_type, task_desc, cron_job_config, _attachmet)
    task_executor.start(task)
    time.sleep(2)
