a,b,v = map(int, input().split())

if (v-a)%(a-b) == 0:
    day = int((v-a)/(a-b))
else:
    day = int((v-a)/(a-b))+1
    
print(int(day)+1)
