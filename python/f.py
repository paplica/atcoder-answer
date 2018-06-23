n,a,b = map(int, input().split())
count = 0
for i in range(n + 1):
  tmp = 0
  for digit in str(i):
    tmp += int(digit)
  if a <= tmp and tmp <= b:
    count += i
print(count)
