class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

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
        if self.parent:
            string = string + str(self.parent.value) + ":"
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
                left_node.parent = root_node
            if right:
                right_node = self.nodes.get(right, Node(right))
                self.nodes[right] = right_node
                root_node.right = right_node
                right_node.parent = root_node

        self.head = self.nodes.get(tuples_lists[0][0])

    def next_inorder_node(self, node):
        if not node.right:
            #am i part of left subtree of my parent ?
            if node.parent.left == node:
                return node.parent
            #am i part of right subtree of my parent ?
            if node.parent.right == node:
                while node.parent.right == node:
                    node = node.parent
                return node.parent
        return node.right

bt = BinaryTree([(10,5,15),(5,3,8),(15,13,17),(3,2,4),(8,7,0),(17,16,0)])
node = bt.next_inorder_node(bt.nodes[16])
print(node)
