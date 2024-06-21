from itertools import combinations
n=int(input())
ls=input().split()
k=int(input())
combination=list(combinations(ls,k))
count=0
for combo in combination:
    if 'a' in combo:
        count+=1
print(count/len(combination))