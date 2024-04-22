n: int = 600851475143
d: int = 2

while n > 1:
    if n % d == 0 & len([i for i in range(2, int(d**0.5) + 1) if n % d == 0]) == 0:
        n //= d

    else:
        d += 1


if __name__ == "__main__":
    print(ans := d)
