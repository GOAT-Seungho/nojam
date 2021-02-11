# 2010 : 플러그

# code for submitting
import sys

N = int(input())
sum = - (N - 1)

for _ in range(N):
    sum += int(sys.stdin.readline())

print(sum)


# solution
# input 자체가 굉장히 많기 때문에 input() 함수로 풀면 시간초과가 난다.
# 따라서 sys.stdin.readline()으로 풀어준다.
# import sys

# tap_num = int(input())
# consent_num = sum([int(sys.stdin.readline()) for _ in range(tap_num)])

# print(consent_num - tap_num + 1)