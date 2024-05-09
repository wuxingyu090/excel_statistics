from dateutil import parser

def __split(keywords, symbol):
    # 使用 split() 方法按逗号分割字符串，并获取分割后的部分
    parts = keywords.split(symbol)
    if len(parts) > 3:
        raise ValueError(str(keywords) + "参数错误!")
    return parts[0],parts[1]


def __gt(ref_value: int, target_value: int) -> int:
    if target_value > ref_value:
        return target_value
    else:
        return None

def __lt(ref_value: int, target_value: int) -> int:
    if target_value < ref_value:
        return target_value
    else:
        return None

def __gtlt(ref_value: str, target_value: int) -> int:
    ltnum, gtnum = __split(ref_value, '-')
    if ltnum < gtnum:
        return ltnum <= target_value < gtnum
    else:
        return target_value >= ltnum or target_value < gtnum
    
def __eq(ref_value: str, target_value: str) -> str:
    if target_value == ref_value:
        return target_value
    else:
        return None

def __match_hour_interval(interval_str, time_str):
    time = parser.parse(time_str)
    start, end = map(int, interval_str.split('-'))
    if start < end:
        return start <= time.hour < end
    else:
        return time.hour >= start or time.hour < end

def __match_day_interval(interval_str, time_str):
    time = parser.parse(time_str)
    start, end = map(int, interval_str.split('-'))
    if start < end:
        return start <= time.day < end
    else:
        return time.day >= start or time.day < end
    
def __match_minute_interval(interval_str, time_str):
    time = parser.parse(time_str)
    start, end = map(int, interval_str.split('-'))
    if start < end:
        return start <= time.minute < end
    else:
        return time.minute >= start or time.minute < end

def filter(keywords: str,string: str) -> str:
    option, parameter = __split(keywords,',')
    if option == '>':
        return __gt(int(parameter),int(string))
    elif option == '<':
        return __lt(int(parameter), int(string))
    elif option == '<>':
        return __gtlt(str(parameter), int(string))
    elif option == '=':
        return __eq(str(parameter), str(string))
    elif option == '%D':
        return __match_day_interval(str(parameter), str(string))
    elif option == '%H':
        return __match_hour_interval(str(parameter), str(string))
    elif option == '%MI':
        return __match_minute_interval(str(parameter), str(string))
    else:
        raise ValueError(str(keywords) + "参数不存在!")
        
    