import inspect
from pprint import pprint


def introspection_info(obj):
    info = {}
    info['Type'] = type(obj)
    info['Attributes'] = []
    info['Methods'] = []
    for item in dir(obj):
        info['Attributes'].append(item) if item[:2] == '__' else info['Methods'].append(item)
    info['Module'] = inspect.getmodule(obj)

    return info

number_info = introspection_info("42")
pprint(number_info)