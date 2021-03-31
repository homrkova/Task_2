N = int(input())
arr = [[0] * N for i in range(N)]
num = 1
i = 0
j = 0
while num <= N ** 2:
    arr[i][j] = num
    if i <= j + 1 and i + j < N - 1:
        j += 1
    elif i < j and i + j >= N - 1:
        i += 1
    elif i >= j and i + j > N - 1:
        j -= 1
    elif i > j and i + j <= N - 1:
        i -= 1
    num += 1
for i in range(len(arr)):
    print(*[arr[i][j] for j in range(len(arr[i]))])
