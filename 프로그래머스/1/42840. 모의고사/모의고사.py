def solution(answers):
    answer = []
    a_answer = 0
    b_answer = 0
    c_answer = 0
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        index = i % len(a)
        if a[index] == answers[i]:
            a_answer +=1
    
        index = i % len(b)
        if b[index] == answers[i]:
            b_answer +=1
    
        index = i % len(c)
        if c[index] == answers[i]:
            c_answer +=1
    answerr = (a_answer, b_answer, c_answer)
    for i in range(len(answerr)):
        if answerr[i] == max(answerr):
            answer.append(i+1)
    return answer