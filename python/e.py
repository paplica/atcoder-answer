a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0
list500 = [ 500*x for x in range(a+1) ]
list100 = [ 100*x for x in range(b+1) ]
list50 = [ 50*x for x in range(c+1) ]
for i in list500:
  for j in list100:
    for k in list50:
      if i + j + k == x:
        count += 1
print(count)

