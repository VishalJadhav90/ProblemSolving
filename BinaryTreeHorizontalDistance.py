class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None


class BinaryTree:
    def __init__(self,tuple_list):
        self.nodes = {}
        self.root = None
        for node_v, left_v, right_v in tuple_list:
            root_node = self.nodes.get(node_v, Node(node_v))
            self.nodes[node_v] = root_node
            if left_v:
                left_node = self.nodes.get(left_v, Node(left_v))
                self.nodes[left_v] = left_node
                root_node.left = left_node
            if right_v:
                right_node = self.nodes.get(right_v, Node(right_v))
                self.nodes[right_v] = right_node
                root_node.right = right_node
        self.root = self.nodes.get(tuple_list[0][0])

    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res+self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def countdistance(self, start, end, res):
        counter = 0
        for i in res:
            if i == start:
                counter = 0
            elif i == end:
                break
            else:
                counter += 1
        return counter


binarytree = BinaryTree([(5, 2, 3), (2, 7, None), (7, 9, None), (3, None, 1), (1, 4, 6)])
print(binarytree.preorder(binarytree.root))
print(binarytree.countdistance(7, 1, binarytree.preorder(binarytree.root)))
