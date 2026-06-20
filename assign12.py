n = int(input())
k = int(input())
arr =list(map(int, input().split()))
window_rotate = arr[-k:] + arr[:-k]
print(window_rotate)