class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


def printList(head):
    node = head
    while node:
        print("node: {}".format(node.val))
        node = node.nxt
    print("")


def insertNode(newNode, newHead):
    if newHead == None:
        newHead = newNode
        return newHead

    node = newHead
    prevNode = node

    while node.nxt and node.nxt.val < newNode.val:
        prevNode = node
        node = node.nxt

    print("{}------->{}".format(newNode.val, node.val))
    if node == newHead:
        if node.val > newNode.val:
            newNode.nxt = node
            newHead = newNode
        else:
            node.nxt = newNode
            newHead = node
    else:
        if not node.nxt:#we are at end
            if node.val > newNode.val:
                newNode.nxt = node
                prevNode.nxt = newNode
            else:
                node.nxt = newNode
        else:#we are at between
            newNode.nxt = node.nxt
            node.nxt = newNode
    printList(newHead)
    return newHead


def sortList(head):
    node = head
    newHead = None

    while node:
        tnxt = node.nxt
        node.nxt = None
        newHead = insertNode(node, newHead)
        node = tnxt
    return newHead


head = None
end = None
for ele in [9, 6, 3, 7, 2, 5, 8, 4, 1]:
    if head == None:
        node = Node(ele, None)
        head = node
        end = node
    else:
        node = Node(ele, None)
        end.nxt = node
        end = end.nxt

#printList(head)
head = sortList(head)
#printList(head)
