

class Node:

    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, key_val_pairs=None):
        self.root = None
        if key_val_pairs:
            for key, val in key_val_pairs:
                self.put(key, val)

    def put(self, key, val):
        self.root = insert_into_tree(self.root, key, val)

    def get(self, key):
        return search_tree(self.root, key)

    def delete(self, key):
        self.root = delete_from_tree(self.root, key)


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


def find_min_in_tree(root):
    curr = root
    while curr.left:
        curr = curr.left

    return curr


def delete_min_from_tree(root):
    if not root.left:
        return root.right

    root.left = delete_min_from_tree(root.left)
    return root


def delete_from_tree(root, key):
    if not root:
        return None

    if root.key < key:
        root.right = delete_from_tree(root.right, key)
    elif root.key > key:
        root.left = delete_from_tree(root.left, key)
    else:
        # if either left or right link is None,
        # the new root should be the other
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        old_root = root
        # set successor of old root as new root
        root = find_min_in_tree(old_root.right)
        # update the links of new root
        root.right = delete_min_from_tree(old_root.right)
        root.left = old_root.left

    return root


def print_in_order(root):
    if not root:
        return
    print_in_order(root.left)
    print(root.key, root.val)
    print_in_order(root.right)


if __name__ == '__main__':
    pairs = [(s, i) for s, i in zip('SEARCHTREE', range(9))]
    bst = BinarySearchTree(pairs)
    print_in_order(bst.root)

    bst.delete('H')
    print_in_order(bst.root)
