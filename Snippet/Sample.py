# In the name of Allah
# Tasnim Jabir

import sys
input = sys.stdin.readline

debug = True
pri = lambda *a, **k: None
if debug:
    import builtins
    pri = builtins.print

t = int(input())
for _ in range(t):
    a = int(input())
    arr = list(map(int, input().split()))
    pri(f"{a, arr = }")


    
    