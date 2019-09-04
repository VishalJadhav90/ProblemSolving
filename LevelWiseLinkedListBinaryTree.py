class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self, tree_node_tuples):
        self.head = None
        self.nodes = {}
        for root, left, right in tree_node_tuples:
            if root not in self.nodes:
                node = Node(root)
                self.nodes[root] = node
            node = self.nodes[root]

            if left not in self.nodes:
                lnode = Node(left)
                self.nodes[left] = lnode
            node.left = self.nodes[left]

            if right not in self.nodes:
                rnode = Node(right)
                self.nodes[right] = rnode
            node.right = self.nodes[right]

        self.root = self.nodes[tree_node_tuples[0][0]]

    def __populate_levelwise_lists(self, node, level, lists):
        if node:
            try:
                levelList = lists[level]
                levelList.append(node.value)
            except IndexError:
                lists.append([])
                lists[level] = [node.value]
            self.__populate_levelwise_lists(node.left, level+1, lists)
            self.__populate_levelwise_lists(node.right, level+1, lists)

    def get_levelwise_lists(self):
        lists = []
        if self.root:
            self.__populate_levelwise_lists(self.root, 0, lists)
        return lists

bt = BinaryTree([(8,6,13), (6,5,7), (13,10,15), (5,4,3)])
print(bt.get_levelwise_lists())