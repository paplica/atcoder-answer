n, y = map(int, input().split())
yukichi = 0
higuchi = n
noguchi = 0
while(higuchi >= 0):
  tmp = yukichi * 10000 + higuchi * 5000 + noguchi * 1000
  if tmp == y:
    print("{} {} {}".format(yukichi, higuchi, noguchi))
    exit()
  if tmp < y:
    higuchi -= 1
    yukichi += 1
  else:
    higuchi -= 1
    noguchi += 1
print ("-1 -1 -1")
