n = int(input())
t0 = 0
x0 = 0
y0 = 0
for i in range(n):
  t,x,y = map(int, input().split())
  diff = abs(x - x0) + abs(y - y0)
  tmp = t - t0 - diff
  if tmp < 0 or tmp%2 == 1:
    print("No")
    exit()
  t0 = t
  x0 = x
  y0 = y
print("Yes")

