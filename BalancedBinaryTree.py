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

    def isBalancedBinaryTree(self, node):
        if not node:
            return 0, True
        left, balanced = self.isBalancedBinaryTree(node.left)
        right, balanced = self.isBalancedBinaryTree(node.right)
        if abs(left-right) > 1 or not balanced:
            return max(left, right) + 1, False
        return max(left, right) + 1, True

bt = BinaryTree([(1,2,3), (2,4,5), (3,6,0), (4,7,8), (7,9,0)])
height, isBalanced = bt.isBalancedBinaryTree(bt.head)
print("height:", height)
print("isBalanced:", isBalanced)
