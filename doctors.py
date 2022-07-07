import json
import os

os.system("clear")

doctors_list_file=open('doctors_list.json')
insurance_list_file=open('insurance_list.json')
insurance_x_doctors_file=open('insurance_x_doctors.json')

doctors_list_file_load= json.load(doctors_list_file)
insurance_list_file_load= json.load(insurance_list_file)
insurance_x_doctors_file_load= json.load(insurance_x_doctors_file)

for cont in doctors_list_file_load:
    docs_x_ins_temp_list=[]
    ins_temp_list=[]
    #Associating Doctors_id with insurance networks
    for cont2 in insurance_x_doctors_file_load:
        if cont['doctor_id']==cont2['doctor_id']:
            docs_x_ins_temp_list.append(cont2['insurance_id'])
    
    for cont3 in insurance_list_file_load:
        if cont3['insurance_id'] in docs_x_ins_temp_list:
            ins_temp_list.append(cont3['name'])

    print(cont['first_name']+" "+cont['last_name'])
    print("Specialities: "+ str(', '.join(cont['specialty']))+'.' )
    print("Address: "+cont['address'])
    print("Associated Insurance network: "+ str(', '.join(ins_temp_list))+'.' )
    print("\n")
