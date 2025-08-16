def merge_dicts_with_overlapping_keys(dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            merged[key] = merged.get(key, 0) + value
    return merged
input1 = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
print(merge_dicts_with_overlapping_keys(input1))
