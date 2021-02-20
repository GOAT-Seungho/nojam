# 1920 : 수 찾기

# code for submitting
import sys

N = int(input())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if (M_list[i] in N_list):
        print(1)
    else:
        print(0)