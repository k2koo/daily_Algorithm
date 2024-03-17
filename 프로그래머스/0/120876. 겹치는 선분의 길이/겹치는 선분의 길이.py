def solution(lines):#min max를 찾고 계산
    starts = [min(a) for a in lines]
    ends = [max(a) for a in lines]
    starts.sort()
    ends.sort()
    answer = 0 
    answer += max(0, ends[0] - starts[1])
    answer += max(0, ends[1] - starts[2])
    answer -= max(0, ends[0] - starts[2])
    return answer
