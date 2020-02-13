class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

    def push(self, new_data):
        new_head = Node(new_data)
        new_head.next = self.head
        self.head = new_head
        self.printlist()


    def insertafter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        self.printlist()

    def deletenode(self, key):
        temp = self.head
        prev_node = temp

        if key == temp.data:
                self.head = None
                return

        while temp:
            next_node = temp.next
            if key == temp.data:
                prev_node.next = next_node
                break
            else:
                prev_node = temp
                temp = temp.next
                continue
        self.printlist()

    def deletelist(self):
        temp = self.head
        next = temp.next

        while temp:
            temp.data = None
            temp = temp.next
        return

if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printlist()
