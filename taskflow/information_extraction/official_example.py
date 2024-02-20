#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from pprint import pprint
from paddlenlp import Taskflow

if __name__ == '__main__':
    schema = ['时间', '选手', '赛事名称'] # Define the schema for entity extraction
    ie = Taskflow('information_extraction', schema=schema)
    results = ie("2月8日上午北京冬奥会自由式滑雪女子大跳台决赛中中国选手谷爱凌以188.25分获得金牌！")
    print(results)