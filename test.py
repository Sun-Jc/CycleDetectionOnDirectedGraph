import sys
from cycle_detect import cycle_detection
import time
import networkx as nx
import random


def test(edges, baseline, title, prob=True):
    start_time = time.time()
    count = 0
    for G, edge, id_node in cycle_detection(edges, baseline=baseline, prob=prob):
        count += 1
        s,t = edge
        s,t = id_node[s], id_node[t]
        print('cycle detected when adding edge {} -> {}'.format(s,t))
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

