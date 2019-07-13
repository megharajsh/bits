import AppConstants
import DoublyLinkedList


class PatientRecord:

    patient_id = AppConstants.PATIENT_ID_NUMBER
    head = None
    tail = None
    patients = []
    doubly_linked_list = None

    def __init__(self, age, name, Pid):
        self.PatId = str(Pid) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None

    # START - Register Patient
    def registerPatient(self, name, age):
        if self.doubly_linked_list is None:
            self.doubly_linked_list = DoublyLinkedList.DoublyLinkedList()
        PatientRecord.patient_id = PatientRecord.patient_id + 1
        new_node = PatientRecord(name, age, self.patient_id)
        self.doubly_linked_list.append(new_node)
        print("\tSuccessfully Registered The Patient - " + new_node.name + ", " + new_node.age + ", " + new_node.PatId)
        self.patients.append(new_node)
        return new_node
    # END - Register Patient

    # START - Enqueue Patient
    def enqueuePatient(self, PatId):
        print('Update Enqueue')
        return self.patients

    def nextPatient(self):
        print("Register The Next Patients")

    def dequeuePatient(self, PatId):
        print("DeQueue Patient")

    def print_items(self):
        self.doubly_linked_list.listprint(self.doubly_linked_list.head)

    def sort_queue(self, patients):
        # Check whether list is empty
        if self.doubly_linked_list.head is None:
            return patients
        else:
            # Current will point to head
            current = self.doubly_linked_list.head
            while current.right is not None:
                # Index will point to node next to current
                index = current.right
                while index is not None:
                    # If current's data is greater than index's data, swap the data of current and index
                    if current.age < index.age:
                        temp_age = current.age
                        temp_name = current.name
                        temp_PatId = current.PatId
                        current.age = index.age
                        current.name = index.name
                        current.PatId = index.PatId
                        index.age = temp_age
                        index.name = temp_name
                        index.PatId = temp_PatId
                    index = index.right
                current = current.right
        return patients




