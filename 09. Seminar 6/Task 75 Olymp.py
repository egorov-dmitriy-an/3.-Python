a = int(input())
m = int(input())
sum = a
n = 1
while True:
    t = (m - sum) / 2
    if t > (a+1):
        a += 1
        sum += a
        n += 1
    elif t == (a+1):
        n += 1
        break
    elif t < (a + 1):
        n = False
        break
print(n)