class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, input_list):
        self.head = None


    def createdlinkedlist(self, input_list):
        for ele in input_list:
            node = Node(ele)
            if self.head == None:
                self.head=node
            else:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=node


    def searchele(self,num_data):
        temp=self.head
        while temp:
            if temp.value==num_data:
                return temp
        return temp

    def print(self):
        pass

obj=LinkedList(input_list=[1,2,3,4,5])
print(obj)
