n , i = list(map(int,input().split()))

if n & 1<<i :
    print("set_bit")
else:
    print("unset_bit")