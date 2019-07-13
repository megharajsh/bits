# Create the doubly linked list class


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    # Define the push method to add elements at the beginning
    def push(self, patient):
        patient_node = patient
        patient_node.right = self.head
        if self.head is not None:
            self.head.left = patient_node
        self.head = patient_node
        return patient_node

    # Define the append method to add elements at the end
    def append(self, patient):
        patient_node = patient
        patient_node.right = None
        if self.head is None:
            patient_node.left = None
            self.head = patient_node
            return
        last = self.head
        while last.right is not None:
            last = last.right
        last.right = patient_node
        patient_node.left = last
        return

    # Define the method to print
    def listprint(self, node):
        while node is not None:
            print(node.PatId),
            last = node
            node = node.right
