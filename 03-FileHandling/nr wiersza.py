a = 1

with open('C:/Users/VG Rig/Desktop/NoEducation.txt','r') as file:
    for line in file:
        print (f'{a}. {line}', end='')
        a+=1