class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        msg = "({},".format(self.value)
        left = "{},".format(self.left.value) if self.left else ","
        right = "{},".format(self.right.value) if self.right else ","
        msg = msg + left + right[:-1] + ')'
        return msg


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

    def __search(self, node, tnode):
        if not tnode:
            return
        if tnode.value == node.value:
            return tnode
        result = self.__search(node, tnode.left)
        if result: return result
        result = self.__search(node, tnode.right)
        if result: return result

    def __match(self, t1, t2):
        if t2 and not t1:
            return False
        if t1 and not t2:
            return True
        if not t1 and not t2:
            return True
        if t1.value != t2.value:
            return False
        return self.__match(t1.left, t2.left) and self.__match(t1.right, t2.right)


    def search_and_match(self, t1):
        match_node = self.__search(self.head, t1.head)
        if match_node:
            return self.__match(match_node, self.head)
        else:
            return False

bt1 = BinaryTree([(10,8,4),(8,6,5),(5,2,0)])
bt2 = BinaryTree([(8,0,5)])
print(bt2.search_and_match(bt1))