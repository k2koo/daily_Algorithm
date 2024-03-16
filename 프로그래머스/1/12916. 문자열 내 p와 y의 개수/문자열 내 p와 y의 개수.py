def solution(s):
    cnt_p = 0
    cnt_y = 0
    for c in s:
        if c == 'p' or c == 'P':
            cnt_p += 1
        elif c == 'y' or c == 'Y':
            cnt_y += 1
    
    
    return  cnt_p == cnt_y