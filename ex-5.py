def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

ans: int = 1

for n in range(1, 21):
    ans = (ans * n)//gcd(ans, n)

print(ans)
