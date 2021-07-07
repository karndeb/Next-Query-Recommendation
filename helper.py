from collections import OrderedDict


def custom_sort(dictionary, key_order):
    items = [dictionary[k] if k in dictionary.keys() else 0 for k in key_order]
    sorted_dict = OrderedDict()
    for i in range(len(key_order)):
        sorted_dict[key_order[i]] = items[i]
    return sorted_dict

