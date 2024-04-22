ans: int = 2
idx: int = 1

while idx != 10_001:
    ans += 1

    if len([d for d in range(2, int(ans**0.5) + 1) if ans % d == 0]) == 0:
        idx += 1

print(ans)
