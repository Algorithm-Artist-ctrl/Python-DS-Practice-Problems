def merge_three_dictionaries(dict1, dict2, dict3):
    merged = {**dict1, **dict2, **dict3}
    print(merged)
dict1={'a': 1, 'b': 2}
dict2={'c': 3, 'd': 4}
dict3={'e': 5, 'f': 6}
merge_three_dictionaries(dict1,dict2,dict3)
