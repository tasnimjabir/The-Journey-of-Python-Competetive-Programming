#Day - 1

a = int(input())
b, c = map(int, input().split())
s = input()
print(str(a+b+c) +" "+ s )

a, b = map(int, input().split())
if (a*b)%2==0:
    print("Even")
else: print("Odd")

s1 = input()
c = 0
for i in s1:
    c+=int(i)
print(c)

n = int(input())
arr = list(map(int, input().split()))
answer = float('inf')
for num in arr:
    count = 0
    while num%2==0:
        num//=2
        count+=1
    answer = min(count, answer)
print(answer)
    


#Day - 2
A, B, C, X = int(input()), int(input()), int(input()), int(input())
cout = 0

for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if (500*i + 100*j + 50*k)==X:
                cout+=1           
print(cout)


N, A, B = map(int, input().split())
res = 0
for i in range(N+1):
    digit_sum = 0
    for num in str(i):
        digit_sum += int(num)
    if A<= digit_sum <=B:
        res+=i
print(res)


#Day - 3
p = 5/3
print(int(p))

s = "12sam"
print(s[2])