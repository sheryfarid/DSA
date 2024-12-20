class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the head
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at a specific position
    def insert_at(self, data, position):
        try:
            if position < 0:
                raise IndexError("Position out of bounds. Negative indices are not allowed.")
            
            new_node = Node(data)
            if position == 0:
                self.insert_head(data)
                return

            temp = self.head
            for _ in range(position - 1):
                if temp is None:
                    raise IndexError("Position out of bounds.")
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        except IndexError as e:
            print(f"Error during insertion: {e}")

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Delete by value
    def delete_by_value(self, value):
        temp = self.head

        # If head node is to be deleted
        if temp and temp.data == value:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        prev.next = temp.next
        temp = None

    # Delete by position
    def delete_by_position(self, position):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        # If the head is to be deleted
        if position == 0:
            self.head = temp.next
            temp = None
            return

        prev = None
        for _ in range(position):
            if temp is None:
                print("Position out of bounds.")
                return
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

    # Display the linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
ll = LinkedList()

ll.insert_head(10)
ll.insert_at("World", 1)
ll.insert_head(20)
ll.insert_at("World", 1)

ll.insert_at("Hello",-1)

# Insert at the end
ll.insert_end("Python")

print("Linked list after insertions:")
ll.display()
