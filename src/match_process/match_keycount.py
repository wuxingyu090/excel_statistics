from src.data_interaction.os_path import OsPathClass
from src.excel_process.excel_general import ExcelGeneralClass
import src.match_process.field_judgment as fj
import re

__reserved_char = ['>,', '<,', '<>,', '=,', '%D,', '%H,', '%MI,']

# 判断子串开头是否是保留字串


def __starts_with_substring(text):
    for substring in __reserved_char:
        if text.startswith(substring):
            return True
    return False

# excel中列表字串转换成列表


def __get_keywords(matchd):
    try:
        keywords = eval(matchd)
        return keywords
    except (SyntaxError, NameError):
        return matchd


# 对单个匹配方式分类匹配过滤数据

def __match_type(field, matchd, data, negation):
    keywords = __get_keywords(matchd)
    if isinstance(keywords, list):
        pattern = rf'\w*({"|".join(map(re.escape, keywords))})\w*'
        filtered_data = [data_dict for data_dict in data if bool(re.search(
            pattern, data_dict.get(field))) == negation]
        return filtered_data
    elif isinstance(keywords, str):
        if __starts_with_substring(keywords):
            filtered_data = [data_dict for data_dict in data if bool(fj.filter(
                keywords, data_dict.get(field))) == negation]
            return filtered_data
        else:
            pattern = rf'\w*{re.escape(keywords)}\w*'
            filtered_data = [data_dict for data_dict in data if bool(re.search(
                pattern, data_dict.get(field))) == negation]
            return filtered_data
    else:
        raise ValueError(str(matchd) + " 存在未知错误!")


# 按行分组统计规则循环匹配形成最终数据


def __filter_datas(input_dict: dict, new_data: list) -> list:
    # 数据匹配过滤
    def filter_data(number: int, data: list) -> list:
        try:
            field = input_dict.get(f'l{number}_field')
            matchd = input_dict.get(f'l{number}_match')
            if field and matchd:
                negation = True
                if matchd.startswith('not'):
                    negation = False
                    matchd = matchd[4:]
                new_data = __match_type(field, matchd, data, negation)
                return new_data
            else:
                return False
        except KeyError as e:
            print(f"Error: {e}")
            return False
    number = 1
    while True:
        data = filter_data(number, new_data)
        if data is None:
            new_data = data
            break
        elif data is False:
            break
        else:
            number += 1
            new_data = data
    return new_data

# 规则表逐行统计规则


def cycle_statistics(input_data: list) -> list:
    try:
        count_list = []
        for index, input_dict in enumerate(input_data):
            ospath = OsPathClass(data_file=input_dict['table'])
            data_file = ospath.data_path()
            data_data = ExcelGeneralClass(
                file=data_file, sheet=input_dict['sheet']).read_data()
            data = __filter_datas(input_dict, data_data)
            count_list.append(
                {'count_name': input_dict['count_name'], 'count_row': index+2, 'count_num': len(data), 'count_data': data})
        return count_list
    except UnboundLocalError as e:
        print(f"Error: {e},未匹配到数据")
        return []
