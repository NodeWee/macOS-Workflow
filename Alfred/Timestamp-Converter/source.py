# -*- coding: utf-8 -*-
'''
Alfred Workflow - Timestamp Converter
Project: https://github.com/NodeWee/macOS-Workflow/Alfred/Timestamp-Converter
Version: 2020.01.29

Author: NodeWee (https://nodewee.github.io)
'''

'''
时间戳与格式化时间之间的互相转换
举例：2020/1/29 <--> 1580227200
'''

import time

query = u'{query}'.strip()

def timeStringToTimestamp(time_string):
    # 统一格式
    time_string = time_string.replace(u'/', u'-')
    time_string = time_string.replace(u'.', u':')

    try:
        # foramt time string -> time tuple
        if ':' in time_string:
            time_tuple = time.strptime(time_string, u'%Y-%m-%d %H:%M:%S')
        else:
            time_tuple = time.strptime(time_string, u'%Y-%m-%d')

        # time tuple -> time stamp
        time_stamp = int(time.mktime(time_tuple))
    except Exception as e:
        return False, str(e)

    return True, time_stamp


def timestampToTimeString(timeStamp):
    try:
        time_stamp = int(timeStamp)
        # 时间戳 -> 时间元组
        # - 输出格林威治时间的时间元组
        # time.gmtime()
        # - 输出本地时间的时间元组
        time_tuple = time.localtime(time_stamp)

        # - 自定义格式的时间字符串
        if time_tuple[3] == 0 and time_tuple[4] == 0 and time_tuple[
                5] == 0:  # hour, minute, second
            time_format = u'%Y-%m-%d'
        else:
            time_format = u"%Y-%m-%d %X"
        time_str = time.strftime(time_format, time_tuple)
    except Exception as e:
        return False, str(e)
    return True, time_str


if query.isdigit():
    success, content = timestampToTimeString(query)
else:
    success, content = timeStringToTimestamp(query)
if success:
    result = str(content)
    subtitle = u'Enter 复制到剪贴板'
else:
    result = u''
    subtitle = u'格式举例：1546272000 或 2019/1/1 或 2019-1-1 或 2019/1/1 10:12:50'

print('<?xml version="1.0"?><items><item uid="desktop" arg="' + result +
      '" valid="yes"><title>' + result + '</title><subtitle>' + subtitle +
      '</subtitle><icon>icon.png</icon></item></items>')
