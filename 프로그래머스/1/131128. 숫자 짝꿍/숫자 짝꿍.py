def solution(X, Y):
    x = [0] * 10
    y = [0] * 10
    for digit in X:
        x[int(digit)] += 1
    for digit in Y:
        y[int(digit)] += 1
    result = ''
    for num in range(9, -1, -1):
        common = min(x[num], y[num])
        result += str(num) * common
    if not result:
        return "-1"
    if result[0] == "0":
        return "0"
    return result