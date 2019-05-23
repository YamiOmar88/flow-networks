# Breadth First Search
# Author: Yamila Omar
# 23/5/2019 

class BreadthFirstSearch:
    def __init__(self, G, source_node):
        self.source_node = source_node
        self.bfs_properties = self.bfs(G)

        
    def bfs(self, G):
        ''''''
        properties = {}
        for node in G.nodes:
            properties[node] = {'color': 'white', 'd': float('inf'), 'predecessor': None}
        properties[self.source_node]['color'] = 'gray'
        properties[self.source_node]['d'] = 0
        queued = [self.source_node]
        adj_in, adj_out = G.adjacencyList
        while len(queued) > 0:
            u = queued.pop(0)            
            for node in adj_out[u]:
                if properties[node]['color'] == 'white':
                    properties[node]['color'] = 'gray'
                    properties[node]['d'] = properties[u]['d'] + 1
                    properties[node]['predecessor'] = u
                    queued.append(node)
                properties[u]['color'] = 'black'
        return properties
        
        
    def get_path(self, to_node):
        ''' '''
        path = []
        while True:
            if to_node == self.source_node:
                path.append(self.source_node)
                break
            elif self.bfs_properties[to_node]['predecessor'] == None:
                break
            else:
                path.append(to_node)
                to_node = self.bfs_properties[to_node]['predecessor']
        path.reverse()
        return path