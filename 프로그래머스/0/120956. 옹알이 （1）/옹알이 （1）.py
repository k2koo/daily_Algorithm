def solution(babbling):
    answer = 0
    word = ["aya","ye","woo","ma"] #가능한 4가지 발음
    for i in babbling: #babbling 문자열 요소로 반복
        for s in word: #4가지 발음 요소로 반복
            i = i.replace(s,'3',1) #발음 존재시 1번만 치환
        if i.replace('3','') =='': #치환된 문자열을 ''로 다시                                     치환하여 공백이라면
            answer += 1 #발음가능하다고 판단하여 카운트
    return answer