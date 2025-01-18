def main(n: int):
    def solve(n, at, to):
        if n > 1: solve(n-1, at, 6-at-to)
        print(at, to)
        if n > 1: solve(n-1, 6-at-to, to)
    solve(n, 1, 3)

if __name__ == "__main__":
    main(int(input()))
