def solution(number, limit, power):
    divisors_count_list = []
    answer = 0
    for i in range(1, number + 1):
        count = 0
        sqrt_i = int(i ** 0.5)

        for j in range(1, sqrt_i + 1): 
            if i % j == 0:
                count += 1
                if j != i // j:
                    count += 1

        divisors_count_list.append(count)
    
    for count in divisors_count_list:
        if count <= limit:
            answer += count
        else:
            answer += power
    return answer