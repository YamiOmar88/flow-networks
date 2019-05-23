# Ford-Fulkerson algorithm
# Yamila Mariel Omar
# 23/05/2019

'''
FUNCTION: FordFulkerson(G, startNode='i', endNode='f')
Input variable: G = graph object. Flow network where the edges 
attribute has tuples as keys where (a, b) are edges, and
edge capacities as values.
Input variable: startNode = start node, default "i"
Input variable: endNode = end node, default "f"

Output variable: flow = dictionary maximum flow
Output variable: Gf = dictionary residual network
'''

def FordFulkerson(G, startNode = 'i', endNode = 'f'):
    from copy import deepcopy
    from breadthfirstsearch import BreadthFirstSearch
    
    
    # Initialize flow to zero
    flow = {}
    for k in G.edges.keys():
        flow[k] = 0
    
    # Define residual network    
    Gf = deepcopy(G)
        
    while True:
        # Use breadth-first search to find a path
        bfs = BreadthFirstSearch(Gf, startNode)
        p = bfs.get_path(endNode)
        if len(p) == 0: break
        p = [(p[i],p[i+1]) for i in range(len(p)-1)]
        
        # Get the minimum residual capacity in that path
        cf = [Gf.edges.get(e, 0) for e in p]
        cf = min(cf)
        
        for e in p:
            anti = (e[1], e[0])
            if e in Gf.edges.keys():
                # Update flow
                flow[e] = flow.get(e, 0) + cf
                
                # Update residual network
                Gf.edges[e] = Gf.edges.get(e, 0) - cf
                if Gf.edges[e] == 0: Gf.edges.pop(e, None)
                Gf.edges[anti] = Gf.edges.get(anti, 0) + cf
            else:
                # Update flow
                flow[anti] = flow.get(anti, 0) - cf
                
                # Update residual network
                Gf.edges[e] = Gf.edges.get(e, 0) - cf
                Gf.edges[anti] = Gf.edges.get(anti, 0) + cf
                
    return flow, Gf
                


# Example network from 'Introduction to Algorithms' book                
# V = ['s', 't', 1, 2, 3, 4]
# G = {('s', 1): 16, ('s', 2): 13, (1, 3): 12, (2, 1): 4, (2, 4): 14, (3, 2): 9, (3, 't'): 20, (4, 3): 7, (4, 't'): 4}