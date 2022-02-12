from collections import defaultdict
from email.policy import default


def bfs(n,m,edges,s):

    visited = []
    queue = []
    traversal = []
    adj_list = defaultdict(list)

    visited.append(s)
    queue.append(s)

    for edge in edges:
        adj_list[edge[0]].append(edge[1])



    print(adj_list)


    while queue:
        m = queue.pop(0)
        for node in adj_list[m]:
            if node not in visited:
                visited.append(node)
                queue.append(node)
                traversal.append(node)

    return traversal
    
    



n=5
m=3
edges = [1,2],[1,3],[3,4]
s=1

print(bfs(n,m,edges,s))

