# Capacity
# Author: Yamila Omar
# Date: 22nd May 2018


class Capacity:
    def __init__(self, nodes_capacity, source_node='s', sink_node='t'):
        '''Initializes capacity instance. Input variables: 
        - nodes_capacity: dictionary with nodes as keys and 
        their capacity as values. 
        - source_node: name of the source (or supersource) node. 
        - sink_node: name of the sink (or supersink) node.'''
        self.nodes_capacity = nodes_capacity
        self.source_node = source_node
        self.sink_node = sink_node
        
    
    def get_edges_capacity(self, G, distribution_method):
        '''Method to calculate the edges capacity. Input 
        variables:
        - G: graph object.
        - distribution_method: method chosen to distribute 
        capacity values from nodes to edges. Available options 
        are "degree", "weight" and "capacity".'''
        if distribution_method == "degree":
            return self._get_edges_capacity_degree(G)
        elif distribution_method == "weight":
            return self._get_edges_capacity_weight(G)
        elif distribution_method == "capacity":
            return self._get_edges_capacity_capacity(G)
        else:
            raise ValueError('distribution_method can only be set to "degree", "weight" or "capacity"')
            
    
    def _get_edges_capacity_degree(self, G):
        '''Internal function used to calculate the edges 
        capacity given the out degree of the nodes. Input 
        variable: G: graph object.'''
        in_degree, out_degree = G.degree
        C = dict()
        for edge in G.edges.keys():
            if self.source_node in edge or self.sink_node in edge:
                C[edge] = float('inf')
            else:
                i = edge[0]
                C[edge] = self.nodes_capacity[i] / out_degree[i]
        return C
        
    
    def _get_edges_capacity_weight(self, G):
        '''Internal function used to calculate the edges 
        capacity given the edges weight values. Input 
        variable: G: graph object.'''
        in_strength, out_strength = G.strength
        C = dict()
        for edge in G.edges.keys():
            if self.source_node in edge or self.sink_node in edge:
                C[edge] = float('inf')
            else:
                i = edge[0]
                C[edge] = (G.edges[edge] / out_strength[i]) * self.nodes_capacity[i]
        return C
        
    
    def _get_edges_capacity_capacity(self, G):
        '''Internal function used to calculate the edges 
        capacity given the values of the capacity of 
        customer nodes. Input variable: G: graph object.'''
        ingoing, outgoing = G.adjacencyList
        C = dict()
        for edge in G.edges.keys():
            if self.source_node in edge or self.sink_node in edge:
                C[edge] = float('inf')
            else:
                i, j = edge[0], edge[1]
                divisor = sum([self.nodes_capacity[x] for x in outgoing[i] if x != self.sink_node])
                C[edge] = (self.nodes_capacity[j] / divisor) * self.nodes_capacity[i]
        return C