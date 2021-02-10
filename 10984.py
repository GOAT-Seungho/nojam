# 10984 : 내 학점을 구해줘

# code for submitting
T = int(input())

for _ in range(T):
    N = int(input())
    C_sum = 0
    grade_sum = 0.0

    for _ in range(N):
        C, G = input().split()
        C, G = int(C), float(G)
        C_sum += C
        grade_sum += C * G
    
    grade_avg = grade_sum / C_sum

    print('%d %0.1f' % (C_sum, grade_avg))