n = int(input())
a =list(map(int, input().split()))
freq = {}
for i in a:
    if i in freq:
        freq[i] = freq[i] +1
    else:
      freq[i] = 1
print(freq,end="")