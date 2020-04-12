def gcd_trio(a, b, c):
  return gcd(gcd(a, b), c)

def gcd(a, b):
  if a < b:
    a, b = b, a
  if b == 0:
    memo[a][b] = a
    return memo[a][b]

  if memo[a][b] != 0:
    return memo[a][b]
  else:
    memo[a][b] = gcd(b, a%b)
    return memo[a][b]

K = int(input())
memo = [[0 for _ in range(K + 1)] for _ in range(K + 1)]

total_gcd = 0
for i in range(1, K + 1):
  for j in range(1, K + 1):
    for k in range(1, K + 1):
      total_gcd += gcd_trio(i, j, k)

print(total_gcd)
