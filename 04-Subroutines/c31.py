def reverse(Tab):
    new_tab=[]
    for i in range(0,len(Tab)):
        new_tab.append(Tab[-i-1])
    return new_tab

a=[2, 5, 4, 1, 8, 7, 4, 0, 9]
print(reverse(a))