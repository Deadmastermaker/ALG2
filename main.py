

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(val)

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next
        print()

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.print_list()  # 1 2 3 4 5
linked_list.reverse()
linked_list.print_list()  # 5 4 3 2 1

