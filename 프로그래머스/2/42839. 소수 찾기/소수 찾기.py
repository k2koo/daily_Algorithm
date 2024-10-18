from itertools import permutations
import math

# 소수 판별 함수
def is_prime(n):
    if n < 2:  # 0과 1은 소수가 아님
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # 나누어 떨어지면 소수가 아님
            return False
    return True

def solution(numbers):
    num_set = set()  # 가능한 숫자를 저장할 집합

    # 주어진 숫자 조합으로 순열을 만들어 모든 숫자 생성
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)  # i자리의 순열을 구함
        for p in perms:
            num = int(''.join(p))  # 순열을 하나의 정수로 변환
            num_set.add(num)  # 집합에 추가 (중복 방지)

    # 소수 판별 후 카운트
    prime_count = 0
    for num in num_set:
        if is_prime(num):
            prime_count += 1

    return prime_count
