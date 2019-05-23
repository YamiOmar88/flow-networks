# main.py
# Author: Yamila Omar
# Date: 22nd May 2018

from graphfile import GraphFile
from graph import Graph 
from capacity import Capacity
from fordfulkerson import FordFulkerson


# Input data
# ==========
graph_to_study = input("Choose graph to study: F1, F2 or F3? ")


# Load graph
# ==========
filename = "data/" + graph_to_study + ".txt"
edges = GraphFile(filename).read_edges_from_file()
F = Graph(edges)

# Get edges capacity
# ==================
nodes_capacity = GraphFile("data/nodes_capacity.txt").read_nodes_capacity_from_file()
C = Capacity(nodes_capacity, 'i', 'f')
C_edges = C.get_edges_capacity(F, "weight")

for k,v in C_edges.items():
    if ("i" in k) or ("f" in k):
        pass 
    else:
        C_edges[k] = int(v)
        
C_edges = {k:v for k,v in C_edges.items() if v > 0}

# Flow Network
# ============
flow_network = Graph(C_edges.copy())

antiparallel_edges = flow_network.find_antiparallel_edges()
counter = 100
while len(antiparallel_edges) > 0:
    edge = antiparallel_edges.pop(0)
    anti = (edge[1],edge[0])
    antiparallel_edges.remove( anti )
    w = flow_network.edges[anti]
    flow_network.deleteEdge(anti[0], anti[1])
    flow_network.addEdge(i=edge[1], j=counter, w_ij=w)
    flow_network.addEdge(i=counter, j=edge[0], w_ij=w)
    counter += 1
    
# Maximum Flow
# ============
flow, residual_network = FordFulkerson(flow_network, startNode='i', endNode='f')


# Final flow
# ==========
flow = {k:v for k,v in flow.items() if v > 0}
flow_fraction = {k:round(v/C_edges[k],2) for k,v in flow.items()}

# Total items to produce daily
# ============================
count = 0
for k,v in flow.items():
    if k[1] == "f": count += v 
    
print("Total items to produce per day: ", count)


# Save flow fraction
# ==================
filename = "results/flow_fraction_" + graph_to_study + ".txt" 
outFile = GraphFile(filename)
outFile.write_graph_to_file(flow_fraction)