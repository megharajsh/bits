import AppConstants
import heapq


class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): return self.val == other.val
  def __str__(self): return str(self.val)

class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self,x): heapq.heappush(self.h,x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self,i): return self.h[i]
  def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
  def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self,i): return self.h[i].val
    
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




