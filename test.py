import sys
from cycle_detect import cycle_detection
import time
import networkx as nx
import random


class counting:
    def __init__(self):
        self.count = 0

def process_G(G, edge, id_node, storage):
    s,t = edge
    s,t = id_node[s], id_node[t]
    storage.count += 1
    print('cycle detected when adding edge {} -> {}'.format(s,t))
    return G


def test(edges, baseline, title, prob=True):
    start_time = time.time()
    count = 0
    
    cycle_detection(edges, process_G, counting(), baseline=baseline, prob=prob)
        
    end_time = time.time()
    print('\n{} method \n time used: {}s \n {} cycle detected'.format(title, int(end_time-start_time), count))


if __name__ == '__main__':
    N = int(sys.argv[1])
    M = int(sys.argv[1])

    edges = []
    for i in range(M):
        s,t = (random.randrange(N), random.randrange(N))
        edges.append((s,t))

    test(edges, True, 'Baseline method')
    print('\n\n\n')
    test(edges, False, 'Õ(m√n) method')

