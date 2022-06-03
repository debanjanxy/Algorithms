"""
@file   kruskal.py
@author (original JAVA) William Fiset, william.alexandre.fiset@gmail.com
        (conversion to Python) Debanjan Das, iamdebanjandas@outlook.com
@date   Jun 3, 2022
@version 0.1
@brief  Kruskal's minimum spanning tree algorithm using Union-Find data structure.
"""

from union_find import UnionFind

def kruskal_mst(num_vertices, edges):
    # Sort the edges based on weights
    edges = dict(sorted(edges.items(), key=lambda x: x[1]))

    # Use union find on disjoint sets
    uf = UnionFind(num_vertices)
    mst = {}
    for edge, cost in edges.items():
        u, v = edge
        ret = uf.union(u, v)
        if ret == 0:
            mst[edge] = cost
    return mst


if __name__ == "__main__":
    edges = {
        (0, 1): 2,
        (1, 2): 3,
        (2, 3): 1,
        (1, 3): 2,
        (4, 5): 4,
        (4, 6): 3,
        (5, 6): 2,
        (2, 4): 1,
    }
    num_vertices = 7
    mst = kruskal_mst(num_vertices, edges)
    print(mst)

