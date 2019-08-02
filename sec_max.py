if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    m=max(arr)
    l=[]
    
    for i in arr:
        if (i!=m):
            l.append(i)

    print max(l)


    
