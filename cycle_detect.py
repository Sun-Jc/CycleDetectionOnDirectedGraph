import networkx as nx
import random
import math
import sys
from tqdm import tqdm as tqdm_no_notebook
from tqdm import tqdm_notebook


def cycle_detection(edges, process_G, storage, baseline=False, progress=True, prob=True):

    tqdm = tqdm_notebook if 'ipykernel' in sys.modules else tqdm_no_notebook
    if not progress:
        tqdm = lambda x: x

    nodes = set()
    for s,t in edges:
        nodes.add(s)
        nodes.add(t)
    N = len(nodes)
    M = len(set(edges))
    deg_threshold = 2 * M / N

    
    node_id = dict(zip(list(nodes), range(N)))
    id_node = dict([(node_id[nid], nid) for nid in node_id.keys()])
    original_edges = edges
    edges = []
    for s,t in tqdm(original_edges):
        edges.append((node_id[s], node_id[t]))
    
    G = nx.DiGraph()
    G.add_nodes_from(list(range(N)))
    
    sample_prob_threshold = math.log(N) / math.sqrt(N) if prob else 1
    S = set([i for i in range(N) if random.random() <= sample_prob_threshold])

    A = [set([i]) for i in range(N)]
    D = [set([i]) for i in range(N)]
    As = [set([i]).intersection(S) for i in range(N)]
    Ds = [set([i]).intersection(S) for i in range(N)]

    AA = [set([i]) for i in range(N)]

    logs = []

    def backable_add(obj, element):
        if element not in obj:
            obj.add(element)
            logs.append((obj, element))

            
    def update(a,b):
        a_ancestors = [x for x in nx.ancestors(G, a)] + [a]
        b_descendants = [x for x in nx.descendants(G, b)] + [b]
        
        for s in b_descendants:
            if s in S:
                for anc in a_ancestors:
                    backable_add(A[s], anc)
                    backable_add(Ds[anc], s)
        for s in a_ancestors:
            if s in S:
                for des in b_descendants:
                    backable_add(D[s], des)
                    backable_add(As[des], s)

            
    def is_s_equivalent(u,v):
        return len(As[u]) == len(As[v]) and len(Ds[u]) == len(Ds[v])
            
        
    def check(a,b):
        to_explore = set([b])
        while len(to_explore) > 0:
            w = to_explore.pop()
            if w == a:
                return False
            if w in AA[a]:
                return False
            elif a in AA[w]:
                pass
            elif not is_s_equivalent(a, w):
                pass
            else:
                backable_add(AA[w], a)
                for w,z in G.out_edges(w):
                    to_explore.add(z)
        return True


    if baseline:
        for s,t in tqdm(edges):
            G.add_edge(s,t)
            if not nx.is_directed_acyclic_graph(G):
                G = process_G(G, (s,t), id_node, storage)
                #yield G, (s,t), id_node
    else:
        dense = False
        for s,t in tqdm(edges):
            G.add_edge(s,t)
            update(s,t)
            if not check(s,t):
                #yield G, (s,t), id_node
                G = process_G(G, (s,t), id_node, storage)
                # rollback
                while len(logs) > 0:
                    obj, element = logs.pop()
                    obj.remove(element)
                G.remove_edge(s,t)
            elif not dense:
                for degree in [G.degree(s), G.degree(t)]:
                    if degree > deg_threshold:
                        print('warning: too dense')
                        dense = True
                
        
    if not nx.is_directed_acyclic_graph(G):
        print('fail to pass: not a DAG finally')
    
    
