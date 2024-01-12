# 从一个复杂结构tdata中按照选择器解析你的数据为dict
# selector 是选择器
# tdata是 复杂结构
# 解析成一个dict

import copy
def fresh_parse_data(selector=None, tdata=None, return_ids=False, extra_keys=None):
    """
    get the data by selector, but if the data is edit already, then merge the edit data to it

    :param selector: the selector of the data which you want to get
    :param tdata: : the total tdata
    :return: {selector: data}
    """
    tdata_copy = copy.deepcopy(tdata)
    fresh_data = fresh_parse.Parser. \
        fresh_parse(selector=selector, tdata=tdata_copy).values()[0]
    extra_values = {}
    if isinstance(fresh_data, dict) and "SALMON_KEY" in fresh_data:
        if extra_keys:
            assert extra_keys, list
            for key in extra_keys:
                extra_values[key] = fresh_data[key]
        fresh_data = fresh_data['SALMON_KEY']

    ids = []
    if isinstance(fresh_data, list) and all(isinstance(d, dict) for d in fresh_data):
        map(lambda x: ids.append({"__id": x.pop("__id", None)}), fresh_data)
    elif isinstance(fresh_data, dict):
        ids.append(fresh_data.pop("__id", None))
    else:
        pass
    if return_ids:
        if extra_keys:
            return ids, fresh_data, extra_values
        else:
            return ids, fresh_data
    else:
        if extra_values:
            return fresh_data, extra_values
        else:
            return fresh_data