m = int(input())
d = {}
r = set()
for i in range(m):
    d[i+1] = [0]*m
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    d[a][b-1] = 1
    d[b][a-1] = 1
def f(x):
    for i in range(m):
        if d[x][i] == 1:
            d[x][i] = 0
            r.add(i+1)
            f(i+1)
f(1)
try:
    r.remove(1)
except:
    pass
print(len(r))

# import networkx as nx

# G = nx.Graph()
# G.add_nodes_from(list(range(int(input()))))
# n = int(input())
# for i in range(n):
#     a,b = map(int,input().split())
#     G.add_edge(a,b)
# print(len(nx.descendants(G, 1)))