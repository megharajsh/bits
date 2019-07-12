import AppConstants
import PatientRecord


class AppUtils:
    def __init__(self):
        print('Initializing')

    @staticmethod
    def write_output_file(full_patients, next_patient):
        print('\nAfter Patient Sorting Writing To File')
        print('--------------------------------------------------------------------')
        next_patient_output_file = open(AppConstants.NEXT_PATIENT_OUTPUT_FILE_NAME, "a")
        file_content = "-----new patient entered--------\nPatient details:\n"
        next_patient_output_file.writelines(file_content)
        print("Writing Record - " + next_patient.name)
        next_patient_output_file.writelines(next_patient.name + ', ' + next_patient.age + ', '
                                            + next_patient.PatId + '\n')
        """
           Sort All Patients Based On The Age In Descending Order
        """
        print('\nAfter Sorting Patients By Age In Descending Order:')
        print('--------------------------------------------------------------------')
        full_patients = PatientRecord.PatientRecord.sort_queue(full_patients)
        next_patient_output_file.writelines("\nRefreshed Queue:\n")
        for patient_item in full_patients:
            print("Writing Record - " + patient_item.name)
            next_patient_output_file.writelines(patient_item.PatId + ', ' + patient_item.name + '\n')
        next_patient_output_file.writelines("--------------------------\n-----------next patient------------\n")
        next_patient_output_file.writelines("Next patient for consultation is: " + full_patients[0].PatId + ", "
                                            + full_patients[0].name + "\n"
                                            + "------------------------------------\n\n")
        next_patient_output_file.close()
