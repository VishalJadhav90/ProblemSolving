class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        msg = "({},".format(self.value)
        left = "{},".format(self.left.value) if self.left else ","
        right = "{},".format(self.right.value) if self.right else ","
        msg = msg + left + right
        return msg[:-1] + ")"


class BinaryTree:
    def __init__(self, list_of_nodes):
        self.head = None
        self.nodes = {}
        for node_v, left_v, right_v in list_of_nodes:
            node = self.nodes.get(node_v, Node(node_v))
            self.nodes[node_v] = node
            if left_v:
                left = self.nodes.get(left_v, Node(left_v))
                self.nodes[left_v] = left
                node.left = left
            if right_v:
                right = self.nodes.get(right_v, Node(right_v))
                self.nodes[right_v] = right
                node.right = right
        self.head = self.nodes[list_of_nodes[0][0]]

    def __str__(self):
        msg = ""
        for node in self.nodes.values():
            msg = msg + "{} ".format(node)
        return msg

    def set_preorder_traversal(self):
        self.preorder = []
        self.preorder_traversal(self.head, self.preorder)
        print(self.preorder)

    def preorder_traversal(self, node, preorder_list):
        if not node:
            return
        preorder_list.append(node.value)
        if node.left:
            self.preorder_traversal(node.left, preorder_list)
        elif node.right:
            preorder_list.append('x')
        if node.right:
            self.preorder_traversal(node.right, preorder_list)
        elif node.left:
            preorder_list.append('x')

    @classmethod
    def issubtree(cls, t1, t2):
        try:
            index = t1.preorder.index(t2.preorder[0])
        except ValueError:
            return False
        for idx in range(0, len(t2.preorder)):
            if t2.preorder[idx] == 'x':
                index += 1
                continue
            if t2.preorder[idx] != t1.preorder[index]:
                return False
            index += index
        return True

bt1 = BinaryTree([(10,8,4),(8,6,5),(5,2,0)])
bt1.set_preorder_traversal()
bt2 = BinaryTree([(8,0,5)])
bt2.set_preorder_traversal()
print(BinaryTree.issubtree(bt1, bt2))
