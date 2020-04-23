if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    a = max(arr)
    for i in range(n):
        if a == max(arr) :
            arr.remove(max(arr))
    print(max(arr))

