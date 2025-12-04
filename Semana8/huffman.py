# Implementación simple de Huffman: construir árbol, generar códigos, codificar y decodificar.
import heapq
from collections import Counter

class Node:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(f, s) for s,f in freq.items()]
    heapq.heapify(heap)
    if len(heap) == 1:
        node = heap[0]
        return Node(node.freq, None, node, None)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        parent = Node(a.freq + b.freq, None, a, b)
        heapq.heappush(heap, parent)
    return heap[0]

def build_codes(root):
    codes = {}
    def _walk(node, prefix):
        if node is None:
            return
        if node.symbol is not None:
            codes[node.symbol] = prefix or '0'
        _walk(node.left, prefix + '0')
        _walk(node.right, prefix + '1')
    _walk(root, '')
    return codes

def encode(text, codes):
    return ''.join(codes[c] for c in text)

def decode(bits, root):
    res = []
    node = root
    for b in bits:
        node = node.left if b == '0' else node.right
        if node.symbol is not None:
            res.append(node.symbol)
            node = root
    return ''.join(res)

if __name__ == '__main__':
    sample = "ABRACADABRA"
    root = build_huffman_tree(sample)
    codes = build_codes(root)
    print('Códigos:', codes)
    enc = encode(sample, codes)
    print('Encoded:', enc)
    dec = decode(enc, root)
    print('Decoded:', dec)