if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    debug = False

    if(debug):
        print(list(arr))
    
    unique_arr = set(arr)

    print(unique_arr)

    