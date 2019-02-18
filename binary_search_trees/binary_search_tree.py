

class Node:

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, key_val_pairs):
        self.root = None
        for key, val in key_val_pairs:
            self.put(key, val)

    def put(self, key, val):
        self.root = insert_into_tree(self.root, key, val)

    def get(self, key):
        return search_tree(self.root, key)


def insert_into_tree(root, key, val):
    if not root:
        return Node(key, val)

    if root.key < key:
        root.right = insert_into_tree(root.right, key, val)
    elif root.key > key:
        root.left = insert_into_tree(root.left, key, val)
    else:
        root.val = val

    return root


def search_tree(root, key):
    if not root:
        return None

    if root.key < key:
        return search_tree(root.right, key)
    elif root.key > key:
        return search_tree(root.left, key)
    else:
        return root.val
