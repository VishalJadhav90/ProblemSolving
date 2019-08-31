sorted_list = [1, 2, 3, 4, 5, 6]


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self, sorted_list):
        self.root = None
        self.root = self.__create_bst(0, len(sorted_list)-1, sorted_list)

    def __create_bst(self, left, right, sorted_list):
        if left < right:
            mid = (left+right+1) // 2
            node = Node(sorted_list[mid])
            node.left = self.__create_bst(left, mid-1, sorted_list)
            node.right = self.__create_bst(mid+1, right, sorted_list)
            return node
        elif left == right:
            node = Node(sorted_list[left])
            return node
        else:
            pass

    def height_bst(self):
        root = self.root
        height = 0
        while root.left:
            height += 1
            root = root.left
        return height

    def __inorder_travesal(self, root):
        if not root:
            return
        self.__inorder_travesal(root.left)
        print(root.value, end=", ")
        self.__inorder_travesal(root.right)

    def print_inorder_traversal(self):
        self.__inorder_travesal(self.root)
        print("")

bst = BST([1, 2, 3, 4, 5, 6])
bst.print_inorder_traversal()
print(bst.height_bst())