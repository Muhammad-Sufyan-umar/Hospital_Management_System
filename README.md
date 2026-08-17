# 🏥 Hospital Management System

A simple **Hospital Management System** built in **Python using Object-Oriented Programming (OOP)**.

This project allows users to manage doctors, patients, and appointments through a simple command-line menu.

## 📌 Features

* Add Doctor
* Add Patient
* Display Doctors
* Display Patients
* Search Patient by ID
* Schedule Appointment
* Display Appointments
* Cancel Appointment
* Exit the system

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Classes and Objects
* Lists
* Loops
* Conditional Statements
* User Input

## 📂 Classes

### `Hospital`

The main class that manages:

* Doctors
* Patients
* Appointments

Methods include:

* `add_doctor()`
* `remove_doctor()`
* `display_doctors()`
* `add_patient()`
* `remove_patient()`
* `display_patients()`
* `search_patient()`
* `schedule_appointment()`
* `display_appointments()`
* `cancel_appointment()`

### `Doctor`

Stores doctor information:

* Doctor ID
* Name
* Specialization

### `Patient`

Stores patient information:

* Patient ID
* Name
* Age
* Disease

It also provides a method to update patient information.

### `Appointment`

Stores appointment information:

* Doctor
* Patient
* Date
* Time

## ▶️ How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/your-username/hospital-management-system.git
```

Go to the project folder:

```bash
cd hospital-management-system
```

Run the Python file:

```bash
python hospital.py
```

## 🖥️ Example Menu

```text
========== Hospital Management System ==========
1. Add Doctor
2. Add Patient
3. Schedule Appointment
4. Display Doctors
5. Display Patients
6. Display Appointments
7. Search Patient by ID
8. Cancel Appointment
9. Exit

Enter your choice 1-9:
```

## 🎯 Purpose of the Project

This project was created to practice **Python OOP concepts** and understand how multiple classes can work together in a real-world application.

It demonstrates relationships between:

```text
Hospital
   ├── Doctors
   ├── Patients
   └── Appointments
```

## 🚀 Future Improvements

Some possible improvements for this project are:

* Add data storage using files
* Add login system
* Add doctor search
* Add patient update option through the menu
* Add appointment validation
* Prevent duplicate doctor and patient IDs
* Add appointment date validation
* Store records permanently using a database

## 👨‍💻 Author

**Muhammad Sufyan**

A Python project created for learning and practicing Object-Oriented Programming.
