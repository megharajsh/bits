import AppConstants
import PatientRecord
from PatientRecord import PatientRecord

if __name__ == '__main__':

    patients = ()

    """
        Read Current Patient File & Creating PatientRecord Object
    """
    currentPatientFile = open(AppConstants.CURRENT_PATIENT_FILE_NAME, "r")
    for patientRow in currentPatientFile:
        patientData = patientRow.rstrip().split(",")
        patient = {
            "name": patientData[0],
            "age": patientData[1].lstrip().rstrip()
        }
        patientRecord = PatientRecord(patient["name"], patient["age"], '')  # type: PatientRecord
        patientRecord.registerPatient(patientRecord.name, patientRecord.age)
    currentPatientFile.close()

    """
        Read Next Patient File & Creating PatientRecord Object
    """
    nextPatientFile = open(AppConstants.NEW_PATIENT_FILE_NAME, "r")
    for patientRow in nextPatientFile:
        if "newPatient:" in patientRow and "," in patientRow:
            validPatientData = patientRow.rstrip().split(":")
            patientData = validPatientData[1].lstrip().rstrip().split(",")
            patient = {
                "name": patientData[0],
                "age": patientData[1].lstrip().rstrip()
            }
            patientRecord = PatientRecord(patient["name"], patient["age"], '')  # type: PatientRecord
            patientRecord.registerPatient(patientRecord.name, patientRecord.age)
    nextPatientFile.close()

