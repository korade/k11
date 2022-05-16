def solve (N, command):
    # Your code goes here
    s=0
    p=[]
    l=[]
    x=[]
    for i in range(N):
        m=command[i]
        if m=="{":
            x.append(i)
            s=0
        elif m=="}":
            for w in range(x[-1],i):
                r=command[w]
                if r[0:6]=="assign":
                    y=r[7]
                    print(s)
                    for e in range(s-1,len(p)):
                        if p[e][0]==y:
                            p.pop(e)
                            
            x.pop()
            #s-=1
        elif m[0:6]=="assign":
            f=[]
            f.append(m[7])
            f.append(m[9:])
            p.append(f)
            s+=1
        elif m[0:5]=="print":
            j=len(p)-1
            while(j>-1):
                if p[j][0] ==m[6]:
                    l.append(p[j][1])
                    break
                j-=1
            if j==-1:
                l.append("undefined")
    return l    



N = int(input())
command = []
for _ in range(N):
    command.append(input())

out_ = solve(N, command)
for i in out_:
    print(i)
#print (' '.join(map(str, out_)))