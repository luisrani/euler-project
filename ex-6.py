ans: int = abs(sum(n**2 for n in range(101)) - sum(n for n in range(101)) ** 2)

if __name__ == "__main__":
    print(ans)
