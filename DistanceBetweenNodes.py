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
            left_node = self.nodes.get(left, Node(left))
            self.nodes[left] = left_node
            right_node = self.nodes.get(right, Node(right))
            self.nodes[right] = right_node
            root_node.left = left_node
            root_node.right = right_node
        self.head = self.nodes.get(tuples_lists[0][0])

    def __create_track(self, node, value, track_list):
        if node and value not in track_list:
            track_list.append(node.value)
            #print("{}, {}".format(node.value, value))
            #print("{}, {}".format(node.left, node.right))
            self.__create_track(node.left, value, track_list)
            self.__create_track(node.right, value, track_list)
            if value in track_list:
                return track_list
            track_list.remove(node.value)

    def FindDistance(self, first, second):
        first_track = self.__create_track(self.head, first, [])
        second_track = self.__create_track(self.head, second, [])
        common_ele = 0
        for idx in range(len(first_track)):
            if first_track[idx] in second_track:
                common_ele = first_track[idx]
                break
        if common_ele:
            first_moves = len(first_track) - first_track.index(common_ele) - 1
            second_moves = len(second_track) - second_track.index(common_ele) - 1
            return first_moves + second_moves
        return 9999999999999999

bt = BinaryTree([(10,20,50), (20,30,40)])
print(bt.FindDistance(40, 50))
