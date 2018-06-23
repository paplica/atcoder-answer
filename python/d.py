n = int(input())
count = 0
list = list(map(int, input().split()))
while True:
  for i in range(n):
    if list[i]%2 != 0:
      print (count)
      exit()
  count += 1
  list = [x//2 for x in list]
