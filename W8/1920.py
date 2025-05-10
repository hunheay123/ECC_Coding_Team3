import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

def main():
    N = int(sys.stdin.readline())
    A = sorted(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    targets = list(map(int, sys.stdin.readline().split()))
    for target in targets:
        print(binary_search(A, target))

if __name__ == "__main__":
    main()