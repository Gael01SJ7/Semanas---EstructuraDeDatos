# tests_mst.py
from mst import GraphMST

def run_tests():
    # Test 1: triangle
    g = GraphMST(3)
    g.add_edge(0,1,10)
    g.add_edge(1,2,10)
    g.add_edge(0,2,15)
    ep, cp = g.prim_mst()
    ek, ck = g.kruskal_mst()
    assert cp == ck == 20, f"Triangle test failed: {cp} vs {ck}"

    # Test 2: example in mst.py
    g2 = GraphMST(4)
    g2.add_edge(0, 1, 10)
    g2.add_edge(0, 2, 6)
    g2.add_edge(0, 3, 5)
    g2.add_edge(1, 3, 15)
    g2.add_edge(2, 3, 4)
    _, c1 = g2.prim_mst()
    _, c2 = g2.kruskal_mst()
    assert c1 == c2, f"Example mismatch: {c1} vs {c2}"

    # Test 3: disconnected graph
    g3 = GraphMST(4)
    g3.add_edge(0,1,1)
    g3.add_edge(2,3,2)
    _, ck3 = g3.kruskal_mst()
    # For disconnected, kruskal returns sum of MSTs of components: expected 3
    assert ck3 == 3, f"Disconnected expected cost 3, got {ck3}"

    print('All tests passed.')

if __name__ == '__main__':
    run_tests()