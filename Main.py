class Hospital:

    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []


    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added to the hospital.")


    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"Patient {patient.name} removed from the hospital.")
        else:
            print(f"Patient {patient.name} not found in the hospital.")


    def display_patients(self):
        if self.patients:
            print("Patients in the hospital:")
            for patient in self.patients:
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}")
        else:
            print("No patients available in the hospital.")


    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"Doctor {doctor.name} added to the hospital.")


    def remove_doctor(self, doctor):
        if doctor in self.doctors:
            self.doctors.remove(doctor)
            print(f"Doctor {doctor.name} removed from the hospital.")
        else:
            print(f"Doctor {doctor.name} not found in the hospital.")



    def display_doctors(self):
        if self.doctors:
            print("Doctors in the hospital: ")
            for doctor in self.doctors:
                print(f"ID: {doctor.doctor_id}, Name: {doctor.name}, Specialization: {doctor.specialization}")
        else:
            print("No doctors available in the hospital.")
    
    
    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print(f"Patient found: ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}")
                return
        print(f"Patient with ID {patient_id} not found.")



    def schedule_appointment(self, doctor, patient, date, time):
        appointment = Appointment(doctor, patient, date, time)
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {patient.name} with Dr. {doctor.name} on {date} at {time}.")


    def display_appointments(self):
        if self.appointments:
            print("Appointments in the hospital:")
            for appointment in self.appointments:
                print(f"Doctor: {appointment.doctor.name}, Patient: {appointment.patient.name}, Date: {appointment.date}, Time: {appointment.time}")
        else:
            print("No appointments scheduled in the hospital.")


    def cancel_appointment(self, appointment):  
            if appointment in self.appointments:
                self.appointments.remove(appointment)
                print(f"Appointment for {appointment.patient.name} with Dr. {appointment.doctor.name} on {appointment.date} at {appointment.time} canceled.")
            else:
                print(f"Appointment not found in the hospital.")
    
    

class Doctor():
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def show_info(self):
        print(f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}")

    

class Patient():
    def __init__(self, patient_id,name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def show_info(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")

    def update_info(self, patient_id=None, name=None, disease=None):
        if patient_id:
            self.patient_id = patient_id
        if name:
            self.name = name
        if disease:
            self.disease = disease
        print(f"Patient information updated: ID: {self.patient_id}, Name: {self.name}, Disease: {self.disease}")


class Appointment():
    def __init__(self, doctor, patient, date, time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time




def Menu():
    obj = Hospital()

    while True:

        print("\n========== Hospital Management System ==========")
        print("1. Add Doctor")
        print("2. Add Patient")
        print("3. Schedule Appointment")
        print("4. Display Doctors")
        print("5. Display Patients")
        print("6. Display Appointments")
        print("7. Search Patient by ID")
        print("8. Cancel Appiontment.")
        print("9. Exit")

        choice = input("Enter your choice 1-9: ")

        # Add Doctor
        if choice == '1':

            doctor_id = input("Enter Doctor ID: ")
            name = input("Enter Doctor Name: ")
            specialization = input("Enter Specialization: ")

            doctor = Doctor(
                doctor_id,
                name,
                specialization
            )

            obj.add_doctor(doctor)

        # Add Patient
        elif choice == '2':

            patient_id = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            disease = input("Enter Disease: ")

            patient = Patient(
                patient_id,
                name,
                age,
                disease
            )

            obj.add_patient(patient)

        # Schedule Appointment
        elif choice == '3':

            if not obj.doctors:
                print("No doctors available.")
                continue

            if not obj.patients:
                print("No patients available.")
                continue

            doctor_id = input("Enter Doctor ID: ")
            patient_id = input("Enter Patient ID: ")

            doctor = None
            patient = None

            # Find doctor
            for d in obj.doctors:
                if d.doctor_id == doctor_id:
                    doctor = d
                    break

            # Find patient
            for p in obj.patients:
                if p.patient_id == patient_id:
                    patient = p
                    break

            if doctor is None:
                print("Doctor not found.")
                continue

            if patient is None:
                print("Patient not found.")
                continue

            date = input("Enter Appointment Date: ")
            time = input("Enter Appointment Time: ")

            obj.schedule_appointment(
                doctor,
                patient,
                date,
                time
            )

        # Display Doctors
        elif choice == '4':
            obj.display_doctors()

        # Display Patients
        elif choice == '5':
            obj.display_patients()

        # Display Appointments
        elif choice == '6':
            obj.display_appointments()

        # Search Patient
        elif choice == '7':

            patient_id = input("Enter Patient ID: ")

            obj.search_patient(patient_id)

        #Cancel appointment
        elif choice =='8':

            if not obj.appointments:
                print("No appointments Availale: ")
                continue

            doctor=input("Enter doctor Name: ")
            patient=input("Enter Patient name: ")
            date=input("Enter date: ")
            time=input("Enter time: ")

            appointment=None

            for i in obj.appointments:
                if (
                    i.doctor.doctor_id==doctor_id
                    and i.patient.patient_id==patient_id
                    and i.date==date
                    and i.time==time):

                    appointment=i
                    break

                if appointment:
                    obj.cancel_appointment(appointment)
                else:
                    print("Appointment Not found..")

        # Exit
        elif choice == '9':
            print("Thank you for using Hospital Management System.")
            break

        else:
            print("Invalid choice. Please enter 1-8.")


Menu()