X,Y,Z=list(map(int,input().split()))
tt=X*Y
tta=Z*1440
if tt<=tta:
    print("YES")
else:
    print("NO")
