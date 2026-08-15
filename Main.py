class Hospital:

    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []


    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added to the hospital.")
    def add_doctor(self, doctorr):
        self.doctors.append(doctorr)
        print(f"Doctor {doctorr.name} added to the hospital.")

    def schedule_appointment(self, doctor, patient, date, time):
        appointment = Appointment(doctor, patient, date, time)
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {patient.name} with Dr. {doctor.name} on {date} at {time}.")

    def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"Patient {patient.name} removed from the hospital.")
        else:
            print(f"Patient {patient.name} not found in the hospital.")

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

    def display_patients(self):
        if self.patients:
            print("Patients in the hospital:")
            for patient in self.patients:
                print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}")
        else:
            print("No patients available in the hospital.")

    def display_appointments(self):
        if self.appointments:
            print("Appointments in the hospital:")
            for appointment in self.appointments:
                print(f"Doctor: {appointment.doctor.name}, Patient: {appointment.patient.name}, Date: {appointment.date}, Time: {appointment.time}")
        else:
            print("No appointments scheduled in the hospital.")

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                print(f"Patient found: ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Disease: {patient.disease}")
                return
        print(f"Patient with ID {patient_id} not found.")

class Doctor():
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization

    def show_info(self):
        print(f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialization: {self.specialization}")

    def show_appointments(self):
        print(f"Appointments for Dr. {self.name}:")
        for appointment in self.appointments:
            if appointment.doctor == self:
                print(f"Patient: {appointment.patient.name}, Date: {appointment.date}, Time: {appointment.time}")


