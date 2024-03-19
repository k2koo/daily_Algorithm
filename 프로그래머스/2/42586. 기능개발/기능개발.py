def solution(progresses, speeds):
    answer = []
    rest = []
    for i in range(len(progresses)):
        remain = (100 - progresses[i]) % speeds[i]
        if remain == 0:
            days = (100 - progresses[i]) // speeds[i]
        else:
            days = (100 - progresses[i]) // speeds[i] +1
        rest.append(days)
    while rest:
        current = rest[0]
        count = 0

        while rest and current >= rest[0]:
            rest.pop(0)
            count += 1
        
        answer.append(count)

    return answer