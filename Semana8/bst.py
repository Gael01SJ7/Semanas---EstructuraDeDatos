# Implementación básica de un BST (sin duplicados) con inserción, búsqueda, eliminación y recorridos.
class Node:
    def __init__(self, key, line_positions=None):
        self.key = key
        self.left = None
        self.right = None
        # positions: list of (line, col) where the word appears (for index)
        self.positions = line_positions or []

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, pos=None):
        def _insert(node, key, pos):
            if node is None:
                node = Node(key, [pos] if pos else [])
                return node
            if key == node.key:
                if pos:
                    node.positions.append(pos)
                return node
            if key < node.key:
                node.left = _insert(node.left, key, pos)
            else:
                node.right = _insert(node.right, key, pos)
            return node
        self.root = _insert(self.root, key, pos)

    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return node
            node = node.left if key < node.key else node.right
        return None

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        def _delete(node, key):
            if node is None:
                return None
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            else:
                # found node
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                # two children: replace with inorder successor
                succ = self._min_node(node.right)
                node.key, node.positions = succ.key, succ.positions
                node.right = _delete(node.right, succ.key)
            return node
        self.root = _delete(self.root, key)

    def inorder(self):
        res = []
        def _inorder(node):
            if not node: return
            _inorder(node.left)
            res.append(node.key)
            _inorder(node.right)
        _inorder(self.root)
        return res

    def preorder(self):
        res = []
        def _pre(node):
            if not node: return
            res.append(node.key)
            _pre(node.left)
            _pre(node.right)
        _pre(self.root)
        return res

    def postorder(self):
        res = []
        def _post(node):
            if not node: return
            _post(node.left)
            _post(node.right)
            res.append(node.key)
        _post(self.root)
        return res

if __name__ == '__main__':
    bst = BST()
    for k in [50,30,70,20,40,60,80]:
        bst.insert(k)
    print('Inorden:', bst.inorder())
    print('Preorden:', bst.preorder())
    print('Postorden:', bst.postorder())
    bst.delete(50)
    print('Inorden tras eliminar 50:', bst.inorder())