seq: list[int] = [1, 2]

while seq[-1] <= 4 * 10e5:
    seq.append(seq[-1] + seq[-2])

ans: int = sum(list(n for n in seq if n % 2 == 0))


if __name__ == "__main__":
    print(ans)
