class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def sorted_insert(self, new_node):
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head
        
    def merge_sorted_lists(self, list1, list2):
        merged_head = Node()
        current = merged_head
        current_list1 = list1.head
        current_list2 = list2.head
        while current_list1 and current_list2:
            if current_list1.data < current_list2.data:
                current.next = current_list1
                current_list1 = current_list1.next
            else:
                current.next = current_list2
                current_list2 = current_list2.next
            current = current.next
        current.next = current_list1 if current_list1 else current_list2
        self.head = merged_head.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Test the implementation
linked_list = LinkedList()
linked_list.append(5)
linked_list.append(3)
linked_list.append(7)
linked_list.append(2)

print("Original list:")
linked_list.display()

# Reverse the linked list
linked_list.reverse()
print("Reversed list:")
linked_list.display()

# Sort the linked list using insertion sort
linked_list.insertion_sort()
print("Sorted list:")
linked_list.display()

# Example of merging sorted linked lists
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.append(8)
list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
list2.append(12)
list2.append(13)

print("Merged sorted lists:")
linked_list.merge_sorted_lists(list1, list2)
linked_list.display()
