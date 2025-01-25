from typing import List

def next_permutation(arr: List):
    n = len(arr)
    i = n - 1
    while i > 0 and arr[i-1] >= arr[i]: i -= 1
    if i == 0: return False
    i,j = i - 1, n - 1
    while arr[i] >= arr[j]: j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    for k in range((n - i) // 2): arr[i+1+k], arr[n-1-k] = arr[n-1-k], arr[i+1+k]
    return True

def main(chars: str):
    arr = list(chars)
    arr.sort()
    res = []
    while True:
        res.append(''.join(arr))
        if not next_permutation(arr):
            break
    print(len(res))
    print('\n'.join(res))

if __name__ == "__main__":
    main(input())