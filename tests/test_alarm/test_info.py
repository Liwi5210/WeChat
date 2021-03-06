# -*- coding: utf-8 -*-
"""
Project: Wechat-Github
Creator: Liwi
Create time: 2021-12-21 16:33
Introduction:
"""
from tests import BaseTestCase
from everyday_wechat.utils import config
from everyday_wechat.utils.data_collection import *
from everyday_wechat.control.airquality.air_quality_aqicn import (
    get_air_quality
)

class TestJobModel(BaseTestCase):
    def test_all_info(self):
        """
        测试获取提醒的所有信息。
        :return:
        """
        girlfriend_infos = config.get('alarm_info').get('girlfriend_infos')
        for gf in girlfriend_infos:
            is_tomorrow = gf.get('is_tomorrow', False)
            calendar_info = get_calendar_info(gf.get('calendar'), is_tomorrow)
            weather = get_weather_info(gf.get('city_name'), is_tomorrow)
            horoscope = get_constellation_info(gf.get("horescope"), is_tomorrow)
            dictum = get_dictum_info(gf.get('dictum_channel'))
            diff_time = get_diff_time(gf.get('start_date'), gf.get('start_date_msg'))
            air_quality = get_air_quality(gf.get('air_quality_city'))

            sweet_words = gf.get('sweet_words')
            send_msg = '\n'.join(
                x for x in [calendar_info, weather, air_quality, horoscope, dictum, diff_time, sweet_words] if x)
            print(send_msg)
            print('\n' + '-' * 50 + '\n')
