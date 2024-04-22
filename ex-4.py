ans: int = 0

for a in range(100, 1000):
    for b in range(100, 1000):
        if ((prod := a * b) > ans) and str(prod)[::-1] == str(prod):
            ans = prod

if __name__ == "__main__":
    print(ans)
