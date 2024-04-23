def prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


t: int = sum(range(2, 2_000_000))
n: int = sum(n for n in range(2, 2_000_000) if not prime(n))

ans: int = t - n

if __name__ == "__main__":
    print(ans)
