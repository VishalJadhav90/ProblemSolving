graph = [[0, 1, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0]]

def __get_adj_nodes(src):
    adj_nodes = []
    nodes = graph[src]
    for i in range(0, len(graph)):
        if nodes[i]:
            adj_nodes.append(i)
    return adj_nodes

def FindPath(src, dst, visited_nodes):
    if src not in visited_nodes and dst not in visited_nodes:
        visited_nodes.append(src)
        for adj_node in __get_adj_nodes(src):
            FindPath(adj_node, dst, visited_nodes)
        if src == dst:
            print(visited_nodes)
        visited_nodes.remove(src)

FindPath(0, 7, visited_nodes=[])
