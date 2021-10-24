# import heapq
import argparse
import random
import time

parser = argparse.ArgumentParser(description="set of batches and servers")
parser.add_argument('--N', type=int)
parser.add_argument('--M', type=int)

args = parser.parse_args()

N = args.N
M = args.M

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class Value_AVL:
    def height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left) - self.height(node.right)

    def minimum_value_node(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.minimum_value_node(node.left)

    def max_value_node(self, node):
        if node is None or node.right is None:
            return node
        else:
            return self.minimum_value_node(node.right)

    def rotate_right(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def rotate_left(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    def insert(self, key, val, root):
        if root is None:
            return Node(key, val)
        elif val <= root.value:
            root.left = self.insert(key, val, root.left)
        elif val > root.value:
            root.right = self.insert(key, val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotate_right(root)
        if balance < -1 and val > root.right.value:
            return self.rotate_left(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def preorder(self, root):
        if root is None:
            return
        print(root.key, root.value)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.key, root.value)
        self.inorder(root.right)

    def delete(self, val, node):
        if node is None:
            return node
        elif val < node.value:
            node.left = self.delete(val, node.left)
        elif val > node.value:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None:
                lt = node.right
                node = None
                return lt
            elif node.right is None:
                lt = node.left
                node = None
                return lt
            rgt = self.minimum_value_node(node.right)
            node.value = rgt.value
            node.right = self.delete(rgt.value, node.right)
        if node is None:
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance > 1 and self.balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node


if __name__ == '__main__':

    ''' Generating random samples
    '''
    start_time = time.time()
    p = []
    for _ in range(N):
        p.append(random.randrange(100, 10000))

    ''' python sort : Timsort(insertion & merge)
    '''
    p.sort(reverse=True)

    avl_tree = Value_AVL()
    root = None
    for i in range(N):
        if i < M:
            root = avl_tree.insert(i, p[i], root)
        else:
            min_node = avl_tree.minimum_value_node(root)
            root = avl_tree.delete(min_node.value, root)

            root = avl_tree.insert(min_node.key, min_node.value + p[i], root)

    min_node = avl_tree.minimum_value_node(root)
    max_node = avl_tree.max_value_node(root)
    print(min_node.value)
    print(max_node.value)

    end_time = time.time() - start_time
    print(end_time)