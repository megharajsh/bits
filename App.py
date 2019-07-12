import AppConstants
import PatientRecord
import AppUtils
from PatientRecord import PatientRecord

if __name__ == '__main__':
    print("App Started\n")

    patients = []
    current_patients = []
    next_patients = []

    """
        Read Current Patient File & Creating PatientRecord Object
    """
    currentPatientFile = open(AppConstants.CURRENT_PATIENT_FILE_NAME, "r")
    print('Reading Content From File: ' + AppConstants.CURRENT_PATIENT_FILE_NAME)
    print('--------------------------------------------------------------------')
    for patientRow in currentPatientFile:
        patientData = patientRow.rstrip().split(",")
        patient = {
            "name": patientData[0],
            "age": patientData[1].lstrip().rstrip()
        }
        patientRecord = PatientRecord(patient["name"], patient["age"], '')  # type: PatientRecord
        current_patient = patientRecord.registerPatient(patientRecord.name, patientRecord.age)
        current_patients.append(current_patient)
    currentPatientFile.close()

    """
       Sort Current Patients Based On The Age In Descending Order
    """
    print('\nAfter Sorting Patients By Age In Descending Order:')
    print('--------------------------------------------------------------------')
    current_patients = PatientRecord.sort_queue(current_patients)
    for item in current_patients:
        print(item.name)

    """
       Write To outputPS5.txt with Refreshed Patient Queue
    """
    print('\nAfter Patient Sorting Writing To File')
    print('--------------------------------------------------------------------')
    current_patient_output_file = open(AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME, "w")
    file_content = "-----Initial Queue--------\nNo of patients added: " + str(len(current_patients))\
                   + "\nRefreshed Queue:\n"
    current_patient_output_file.writelines(file_content)
    for item in current_patients:
        print("Writing Record - " + item.name)
        current_patient_output_file.writelines(item.PatId + ', ' + item.name + '\n')
    current_patient_output_file.close()

    """
        Read Next Patient File & Creating PatientRecord Object
    """
    nextPatientFile = open(AppConstants.NEW_PATIENT_FILE_NAME, "r")
    print('\nReading Content From File:' + AppConstants.NEW_PATIENT_FILE_NAME)
    print('--------------------------------------------------------------------')
    for patientRow in nextPatientFile:
        if "newPatient:" in patientRow and "," in patientRow:
            validPatientData = patientRow.rstrip().split(":")
            patientData = validPatientData[1].lstrip().rstrip().split(",")
            patient = {
                "name": patientData[0],
                "age": patientData[1].lstrip().rstrip()
            }
            patientRecord = PatientRecord(patient["name"], patient["age"], '')  # type: PatientRecord
            next_patient = patientRecord.registerPatient(patientRecord.name, patientRecord.age)
            next_patients.append(next_patient)
            patients = current_patients + next_patients
            AppUtils.AppUtils.write_output_file(patients, next_patient)
    nextPatientFile.close()






