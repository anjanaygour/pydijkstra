#Name:Anjanay Kirti Gour
#Roll No: 2017021
#Section/Group: A-6
def dijstra(connections,weights,source):
    Q=[]
    dist=[]
    for i in range(len(connections)):
        a=float("inf")
        dist.append(a)
        Q.append(i)
    dist[source]=0
    p=dist[:]
    while Q!=[]:
        u1=min(p)
        if u1==float("inf"):
            break
        u2=p.index(u1)
        Q.remove(u2)
        p[u2]=float("inf")
        for i in range(len(connections[u2])):
            alt=dist[u2]+weights[u2][i]
            if alt<dist[connections[u2][i]]:
                dist[connections[u2][i]]=alt
                p[connections[u2][i]]=alt
    return dist
def BFS(connections,weights,source):
    Q=[]
    df=[]
    e=[]
    ql=[]
    for i in range(len(connections)):
        df.append(float("inf"))
        Q.append(i)
    ql.append(source)
    Q.remove(source)
    df[source]=0
    while Q!=[]:
        if ql:
            a=ql.pop(0)
        else:
            return df
        e.append(a)
        for i in connections[a]:
            if i in Q:
                ql.append(i)
                Q.remove(i)
                er=connections[a].index(i)
                df[i]=df[a]+weights[a][er]
    return df
if __name__=="__main__":
    T=int(input())
    connections=[]
    weights=[]
    for i in range(T):
        a=int(input())
        e,f=[],[]
        for j in range(a):
            b=[int(s) for s in input().split()]
            e.append(b[0])
            f.append(b[1])
        connections.append(e)
        weights.append(f)
