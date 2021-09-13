import numpy as np
import scipy.sparse as sps
import networkx as nx

class Neuron:
    # TODO
    def __init__(self, _input, charge):
        self.charge = charge #charge as in excitatory (positive) or inhibitory (negative)
    def refractory_period(self):
        pass
        
        
class CausalGraph:
    """Dynamic network/causal graph/neural network
    Discrete dynamics: if one cell/node is active, any neighbors are activated in the next time step
    """
    def __init__(self, g):
        """
        Initializes network given a networkx graph object
        TODO:        if adj_mat is an int, creates a random ergodic, (scale free?) graph of size adj_mat
        """
        #Neuron.__init__(self, _input) #if inheritting from neuron

        self.g = g            
        self.size = self.adj_mat().shape[1]
        
    def adj_mat(self,dense=True):
        sparse = nx.adjacency_matrix(self.g)
        if dense:
            return sparse.todense()
        else:
            return sparse
        
    def simulate(self, init_neurons, time):
        """
        Simulates the network as a discrete graph dynamical system starting at initially fired neurons
        if init_neurons = 'random', creates a random initial condition
        if init_neurons = 'osc', gives certain neurons random firing frequencies throughout the simulation
        
        Since multiple incoming signals sums linearly, normalizing by in degree so that raster is binary (or just
        changing vals>0 to 1)
        """
        adj_mat = self.adj_mat()     
        if init_neurons == 'random':
            pass #create random binary vector 

        raster = []
        for t in range(1,time+1):
            spikes_at_t = np.linalg.matrix_power(adj_mat.T, t)@init_neurons.T
#             normalized_spikes_at_t = []
#             for i in spikes_at_t[0]:
#                 if i != 0:
#                     normalized_spikes_at_t.append(1)
#                 else:
#                     normalized_spikes_at_t.append(0)
#             raster.append(normalized_spikes_at_t)
            print(spikes_at_t.shape, '\n', spikes_at_t)
            raster.append(spikes_at_t[0])
        return np.array(raster, dtype=int)
    
    def graphStats(self, stat):
        """Uses spectral and algebraic graph theory to extract qualitative descriptions of the graph"""
        laplacian = None
        def connectivity(laplacian):
            c_info = np.linalg.eig(laplacian)
            return c_info
        if stat == 'connectivity':
            pass #return connectivity for eigenvalues w.r.t degree, in-degree and out-degree