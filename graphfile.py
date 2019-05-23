# Useful functions
# Author: Yamila M. Omar
# Date: 4/4/2019
# ======================

class GraphFile:
    def __init__(self, fileName):
        '''Initialize class with name of file.'''
        self.filename = fileName
    
    
    def read_edges_from_file(self):
        '''Read graph from file. The file contains one edge (i,j) 
        and its weight w_ij per line as follows:
        i j w_ij'''
        edges = {}
        with open(self.filename) as fileHandle:
            for line in fileHandle:
                line = line.strip().split()
                if len(line) != 3: continue
                i, j, w_ij = line[0], line[1], line[2]
        
                try:
                    i = int(i)
                except ValueError:
                    pass
        
                try:
                    j = int(j)
                except ValueError:
                    pass
        
                w_ij = float(w_ij)
                edges[(i,j)] = w_ij 
        
        return edges
    
    
    
    def write_graph_to_file(self, G):
        '''Write graph G to file. G must be a dictionary. 
        Keys are tuples (i,j) of edges and values are weights w_ij.'''
        with open(self.filename, 'w') as f:
            for k,v in G.items():
                i, j, w_ij = str(k[0]), str(k[1]), str(v)
                f.write(i + ' ' + j + ' ' + w_ij + '\n')
        return True
    
    
    def read_dictionary_from_file(self, separator=' '):
        '''This function reads a dictionary from a file. The file 
        must contain just two columns: key and value separated by 
        separator (default: space).'''
        my_dict = dict()
        with open(self.filename) as f:
            for line in f:
                line = line.strip().split(separator)
                k, v = line[0], line[1]
                my_dict[k] = v
        return my_dict
    
    
    def read_centrality_values_from_file(self, separator=' '):
        '''Read centrality values from file. The file must contain 
        one node per line and its centrality value as follows:
        i c_i'''
        d = self.read_dictionary_from_file()
        C = dict()
        for k,v in d.items():
            v = float(v)
            try:
                k = int(k)
            except:
                pass
            C[k] = v
        return C
        
    def read_nodes_capacity_from_file(self, separator=' '):
        '''Read nodes capacity from file. The file must contain 
        one node per line and its capacity value: i c_i. The 
        input variable separator (default=' ') allows to handle 
        files where the separator is other than white space. It is 
        currently implemented for integer node names. '''
        d = self.read_dictionary_from_file(separator)
        nodes_capacity = dict()
        for k,v in d.items():
            k,v = int(k), int(v)
            nodes_capacity[k] = v
        return nodes_capacity
    

    def write_centrality_values_to_file(self, C):
        '''Write centrality values to file. C must be a dictionary. 
        Keys are nodes i and values are centrality values c_i.'''
        with open(self.filename, 'w') as f:
            for k,v in C.items():
                i, c_i = str(k), str(v)
                f.write(i + ' ' + c_i + '\n')
        return True