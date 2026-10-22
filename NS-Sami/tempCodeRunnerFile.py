S = input()
i = 0
while i < len(S):
    if S[i] == "d":
        if S[i:i+7]=="dreamer":
            i+=7
        elif S[i:i+5]=="dream":
            i+=5
        else :
            print("NO")
            exit()
    if S[i]== "e":
        if S[i:i+6]=="eraser":
            i+=6
        elif S[i:i+5]=="erase":
            i+=5
        else:
            print("NO")
            exit()
    else : 
        print("NO")
        exit()
print("YES")