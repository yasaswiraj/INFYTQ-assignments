#Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
#{
 #"P":"Pediatrics",
#"O":"Orthopedics",
#"E":"ENT
#}

#Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
#Also write the pytest test cases to test the program.



def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    max_visit=0
    P=patient_medical_speciality_list.count('P')
    E=patient_medical_speciality_list.count('E')
    O=patient_medical_speciality_list.count('O')
    
    if P>E and P>O:
        speciality= medical_speciality['P']
    elif E>O:
        speciality= medical_speciality['E']
    else:
        speciality= medical_speciality['O']
    
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'O',302, 'O' ,305, 'O' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
