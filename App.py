import AppConstants
import PatientRecord
from PatientRecord import PatientRecord

if __name__ == '__main__':
    print("\n\nDoctor Consultation App Started")
    print('_________________________________')

    patients = []
    current_patients = []
    next_patients = []

    """
        Read File, Load Current Patients Record & Create PatientRecord Object
    """
    currentPatientFile = open(AppConstants.CURRENT_PATIENT_FILE_NAME, "r")
    print('\n\n1A. Reading Current Patients From File: \'' + AppConstants.CURRENT_PATIENT_FILE_NAME + '\'')
    print('=============================================================================')
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
    current_patients = patientRecord.sort_queue(current_patients)

    """
       Write To outputPS5.txt with Refreshed Patient Queue
    """
    print('\n\n1B. After Patient Sorting, Writing To File: \'' + AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME + '\'')
    print('=============================================================================')
    current_patient_output_file = open(AppConstants.CURRENT_PATIENT_OUTPUT_FILE_NAME, "w")
    file_content = "\t--------- Initial Queue ---------\n" \
                   + "\tNo of patients added: " + str(len(current_patients)) + "\n" \
                   + "\tRefreshed Queue:\n"
    for item in current_patients:
        file_content = file_content + "\t" + item.PatId + ', ' + item.name + '\n'
    file_content = file_content + "\t----------------------------------"
    print(file_content)
    current_patient_output_file.writelines(file_content)
    current_patient_output_file.close()

    """
        Read File, Load New Patients Record & Create PatientRecord Object
    """
    nextPatientFile = open(AppConstants.NEW_PATIENT_FILE_NAME, "r")
    all_patients_output_file = open(AppConstants.ALL_PATIENT_OUTPUT_FILE_NAME, "w+")
    all_patients_output_file.writelines('')
    all_patients_output_file = open(AppConstants.ALL_PATIENT_OUTPUT_FILE_NAME, "a")
    print('\n\n1C. Reading New Patients From File: \'' + AppConstants.NEW_PATIENT_FILE_NAME + '\'')
    print('=============================================================================')
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
            file_content = "\n\t--------- new patient entered ---------\n" \
                           + "\tPatient details: " \
                           + next_patient.name + ", " + next_patient.age + ", " + next_patient.PatId + "\n" \
                           + "\tRefreshed Queue:\n"
            next_patients.append(next_patient)
            all_patients = current_patients + next_patients
            all_patients = patientRecord.enqueuePatient(next_patient.PatId)
            all_patients = patientRecord.sort_queue(all_patients)
            for patient_item in all_patients:
                file_content = file_content + "\t" + patient_item.PatId + ', ' + patient_item.name + '\n'
            file_content = file_content + "\t----------------------------------------\n"
            print(file_content)
            """
                Write File, Update New Patients With Queue Priority
            """
            all_patients_output_file.writelines(file_content)
    all_patients_output_file.close()






