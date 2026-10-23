s = input()
while s:
    if s.endswith("dreamer"):
        s = s[0:len(s)-7]
    elif s.endswith("eraser"):
        s = s[ :-6]
    elif s.endswith("dream"):
        s = s[ :-5]
    elif s.endswith("erase"):
        s=s[ :-5]
    else:
        print("NO")
        exit()

print("YES")