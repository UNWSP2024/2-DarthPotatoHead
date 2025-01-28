#Program Written By: Ainsley Bellamy
#Date Written: 01/27/2025
#Program Title: displayPersonalInfo

#This program displays fictional address and cellphone info
def personal_information():
#Variables for each item
    name = "Ainsley Bellamy"
#Added \t's to format
    address = "3675 32nd Street South\n\t\t\t\t\t  Denver, CO 80014"
    cellNumber = "303-678-4120"
    major = "Liberal Studies"
#print all variables in one statement
    print(f'Name ---------------- {name}\n'
          f'Address ------------- {address}\n'
          f'Cell Phone Number --- {cellNumber}\n'
          f'College Major ------- {major}\n')

personal_information()