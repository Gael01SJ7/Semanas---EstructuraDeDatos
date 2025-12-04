# Implementación de AVL con rotaciones y operaciones básicas.
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def height_of(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.height_of(node.left), self.height_of(node.right))

    def balance_factor(self, node):
        return self.height_of(node.left) - self.height_of(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    def _insert(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        self.update_height(node)
        bf = self.balance_factor(node)
        # LL
        if bf > 1 and key < node.left.key:
            return self.rotate_right(node)
        # RR
        if bf < -1 and key > node.right.key:
            return self.rotate_left(node)
        # LR
        if bf > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # RL
        if bf < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def _delete(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        self.update_height(node)
        bf = self.balance_factor(node)
        # Balancing
        if bf > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        if bf > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if bf < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        if bf < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def inorder(self):
        res=[]
        def _in(n):
            if not n: return
            _in(n.left); res.append(n.key); _in(n.right)
        _in(self.root)
        return res

if __name__ == '__main__':
    a = AVL()
    for k in [30,20,25]:
        a.insert(k)
    print('AVL inorden:', a.inorder())
    a.insert(10); a.insert(40); a.insert(50)
    print('AVL inorden after inserts:', a.inorder())
    a.delete(20)
    print('AVL inorden after delete 20:', a.inorder())