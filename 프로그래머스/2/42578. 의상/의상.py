def solution(clothes):
    items = {}
    for item in clothes:
        value, key = item
        if key in items:
            items[key].append(value)
        else:
            items[key] = [value]

    product = 1
    for key in items:
        num = len(items[key]) + 1
        product *= num
    result = product - 1
    return result