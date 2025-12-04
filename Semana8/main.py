import sys, re
from bst import BST
from huffman import build_huffman_tree, build_codes, encode

def build_index(filename):
    bst = BST()
    with open(filename, 'r', encoding='utf-8') as f:
        for line_no, line in enumerate(f, start=1):
            words = re.findall(r"\w+", line.lower())
            for col, w in enumerate(words, start=1):
                bst.insert(w, pos=(line_no, col))
    return bst

def compress_file(filename, out_huff='out.huff'):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    root = build_huffman_tree(text)
    codes = build_codes(root)
    bits = encode(text, codes)
    with open(out_huff, 'w', encoding='utf-8') as fo:
        fo.write(bits)
    return root, codes

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python3 main.py texto_1000_palabras.txt')
        sys.exit(1)
    filename = sys.argv[1]
    print('Construyendo índice (BST)...')
    index = build_index(filename)
    print('Palabras únicas en índice (primeras 20):', index.inorder()[:20])
    print('Corriendo Huffman...')
    root, codes = compress_file(filename, out_huff='sample.huff')
    print('Códigos Huffman (primeros 20 símbolos):', dict(list(codes.items())[:20]))
    print('Archivo comprimido sample.huff creado (contenido en bits, no binario actual)')