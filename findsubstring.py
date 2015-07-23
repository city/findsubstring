nstr = "fornassis"
substr = "nss"

Found = False
i = 0
while(i < len(mainstr)-1-len(substr) and not Found):
    j= i + len(substr)
    mstr = ""

    for p in range(i, j):
        mstr += mainstr[p]
    i += 1
    if(mstr == substr):
        Found = True
print(Found)
