ans: int = 0

for a in range(1, 1000):
    for b in range(1, 1000):
        c = (a**2 + b**2) ** 0.5

        if a + b + c == 1000 and a**2 + b**2 == c**2:
            ans = int(a * b * c)

if __name__ == "__main__":
    print(ans)
