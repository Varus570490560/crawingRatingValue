import string
import re


def slug_proc(slug: string):
    if slug.endswith('-mod-apk'):
        slug = slug.replace('-mod-apk', '')
    elif slug.endswith('-mod'):
        slug = slug.replace('-mod', '')
    elif slug.endswith('-apk-mod'):
        slug = slug.replace('-apk-mod', '')
    elif slug.endswith('-apk'):
        slug = slug.replace('-apk', '')
    return slug


def find_value(source):
    value_str = ""
    begin_index = source.find('ratingValue') + 13
    end_index = source.find(',', begin_index) - 1
    if begin_index != 12:
        i = begin_index
        while i <= end_index:
            value_str += source[i]
            i += 1
    if value_str == "":
        return -1
    return float(value_str)


def find_value_mc(source):
    value_str = ""
    begin_index = source.find('user large game mixed') + 23
    end_index = source.find('<', begin_index) - 1
    if begin_index != 22:
        i = begin_index
        while i <= end_index:
            value_str += source[i]
            i += 1
    if value_str == "":
        return -1
    if is_float(value_str):
        return float(value_str)
    else:
        return -1


def is_float(s):
    pattern = '^-?\d+\.?\d*$'  # 匹配数字: 从头开始匹配 -0或1次 数字1或多次 .0或1次 数字0或多次 匹配到字符串末尾
    match = re.match(pattern, s)
    return match is not None


def find_value_mc_2(source):
    value_str = ""
    begin_index = source.find('user large game positive') + 26
    end_index = source.find('<', begin_index) - 1
    if begin_index != 25:
        i = begin_index
        while i <= end_index:
            value_str += source[i]
            i += 1
    if value_str == "":
        return -1
    if is_float(value_str):
        return float(value_str)
    else:
        return -1
