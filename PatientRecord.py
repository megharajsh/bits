import AppConstants


class PatientRecord:

    patient_id = AppConstants.PATIENT_ID_NUMBER
    head = None
    tail = None

    def __init__(self, age, name, Pid):
        self.PatId = str(Pid) + str(age)
        self.name = name
        self.age = age
        self.left = None
        self.right = None

    # START - Register Patient
    def registerPatient(self, name, age):
        PatientRecord.patient_id = PatientRecord.patient_id + 1
        new_node = PatientRecord(name, age, self.patient_id)
        if self.head is None:
            new_node.left = None
            self.head = new_node
        else:
            current_node = self.head
            while current_node.right:
                current_node = current_node.right
            current_node.right = new_node
            new_node.left = current_node
            new_node.right = None
        print("Successfully Registered The Patient - " + new_node.name + "(" + new_node.PatId + ")")
        return new_node
    # END - Register Patient

    def nextPatient(self):
        print("Register The Next Patients")

    def _dequeuePatient(self, PatId):
        print("DeQueue Patient")

    @staticmethod
    def sort_queue(patients):
        return patients




