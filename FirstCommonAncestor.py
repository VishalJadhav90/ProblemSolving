class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        string = "{}:".format(self.value)
        if self.left:
            string = string + str(self.left.value) + ":"
        else:
            string = string + "0" + ":"
        if self.right:
            string = string + str(self.right.value) + ":"
        else:
            string = string + "0" + ":"
        return string

class BinaryTree:
    def __init__(self, tuples_lists):
        self.nodes = {}
        self.head = None
        for node, left, right in tuples_lists:
            root_node = self.nodes.get(node, Node(node))
            self.nodes[node] = root_node
            if left:
                left_node = self.nodes.get(left, Node(left))
                self.nodes[left] = left_node
                root_node.left = left_node
            if right:
                right_node = self.nodes.get(right, Node(right))
                self.nodes[right] = right_node
                root_node.right = right_node

        self.head = self.nodes.get(tuples_lists[0][0])

    def find_path(self, node1, path1, node2, path2, node):
        if node:
            if node1 not in path1: path1.append(node)
            if node2 not in path2: path2.append(node)
            if node1 not in path1 or node2 not in path2:
                self.find_path(node1, path1, node2, path2, node.left)
                self.find_path(node1, path1, node2, path2, node.right)
            if node1 not in path1: path1.remove(node)
            if node2 not in path2: path2.remove(node)

    def first_common_ancestor(self, node1, node2):
        path1 = []
        path2 = []
        self.find_path(node1, path1, node2, path2, self.head)
        smallpath = len(path1) if len(path1) < len(path2) else len(path2)
        common_first_acestor = None
        for i in range(smallpath):
            if path1[i] == path2[i]:
                common_first_acestor = path1[i]
        return common_first_acestor

bt = BinaryTree([(10,5,15),(5,3,8),(15,13,17),(3,2,4),(8,7,0),(17,16,0)])
node = bt.first_common_ancestor(bt.nodes[5], bt.nodes[16])
print(node)
