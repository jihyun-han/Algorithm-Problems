import sys
T = int(sys.stdin.readline())
stc = []
for i in range(T):
    stc.append(sys.stdin.readline().strip())

stc = list(set(stc))
stc.sort()
stc.sort(key = len)


for i in stc:
    print(i)
