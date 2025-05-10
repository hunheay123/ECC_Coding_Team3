import sys
from collections import Counter

def main():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    counter = Counter(A)
    M = int(sys.stdin.readline())
    targets = list(map(int, sys.stdin.readline().split()))
    for target in targets:
        print(counter.get(target, 0), end=' ')

if __name__ == "__main__":
    main()