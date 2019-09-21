class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

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

    def isBinaryTreeBST(self, node):
        if not node:
            return True, -1
        if not node.left and not node.right:
            return True, node.value
        leftStatus, leftValue = self.isBinaryTreeBST(node.left)
        rightStatus, rightValue = self.isBinaryTreeBST(node.right)
        if leftStatus and rightStatus and leftValue < node.value < rightValue:
            return True, node.value
        else:
            return False, node.value

bt = BinaryTree([(10,11,15), (5, 3, 8), (15, 13, 17), (8, 7, 9)])
result, _ = bt.isBinaryTreeBST(bt.head)
print(result)
