tablica=[32,16,5,8,24,7]

with open ('C:/Users/VG Rig/Desktop/Tablica.txt','w') as file:
    for x in tablica:
        file.write(str(x)+'\n')