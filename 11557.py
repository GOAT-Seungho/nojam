# 11557 : Yangjojang of The Year

# code for submitting
T = int(input())

for _ in range(T):
    N = int(input())

    y = {}

    for _ in range(N):
        S, L = input().split()
        L = int(L) 
        y[L] = S
    
    print(y[max(y.keys())])


# solution 
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     alcohol = []
    
#     for _ in range(N):
#         S, L = map(str, input().split())
#         alcohol.append([S,int(L)])
        
#     alcohol = sorted(alcohol, key = lambda x: x[1])
#     print(alcohol[-1][0])