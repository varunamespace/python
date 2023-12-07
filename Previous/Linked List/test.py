
def sumdiagonal(l):
     l1 = []
     l2 = []
     sum1 = 0
     sum2 = 0
     for i in range(0, len(l), 4):
          l1.append(l[i])
          res = res + sum(l1)
          sum1 = sum1 + l[i]

     for j in range(2, len(l) - 2, 2):
          l2.append(l[j])
          res2 = sum(l2)
          sum2 = sum2 + l[i]
     fsum = abs(sum1 - sum2)
     return fsum

l = [1,2,3,4,5,6,9,8,9]
print(sumdiagonal(l))

def sumdiagonal(l):
     l1 = []
     l2 = []
     sum1 = 0
     sum2 = 0
     for i in range(0, len(l), n+1):
          l1.append(l[i])
          res = sum(l1)
          sum1 = sum + l[i]

     for j in range(n-1, len(l) - n-1, n-1):
          l2.append(l[j])
          res2 = sum(l2)

     fsum = abs(res - res2)
     return fsum
