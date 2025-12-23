
Sab_tuple=(1,4,9,"sabarnaChatterjee",False,[10,30,50],[44,33,55,77,88])
print (Sab_tuple)
print(Sab_tuple[:6])
print(Sab_tuple[1:])
print(Sab_tuple[3])
print(Sab_tuple[5][2])
print(len(Sab_tuple))
print(Sab_tuple[3]*3)
print(Sab_tuple+(3,33,333))

SAB_Set1 = {1,6,5,3}
SAB_Set2 = {11,6,5,13}
union_set = SAB_Set1 | SAB_Set2
print (union_set)
Intersec_set = SAB_Set1 & SAB_Set2
print (Intersec_set)
Diff_set = SAB_Set1 - SAB_Set2
print (Diff_set)
SemDif_set = SAB_Set1 ^ SAB_Set2
print (SemDif_set)


My_List = [1,45,70,303]
My_List.append(4)  #Append uses to add value at the last of the list
print (My_List)

My_List = [1,45,70,303]
My_2ndList = [11,450,700,3030]
My_List.extend(My_2ndList) # Here we concate 2 list together .
print (My_List)
My_List.insert(4,99999)  # Here we insert a value in to the list we need 2 things one is the position
print (My_List)
My_List.remove(303) # Remove the Perticular value that you want
print (My_List)
print (My_List.pop()) # print the last value of the
print (My_List.clear())

My_List22 = [1,9,5,4,2,929,33,12,45,70,303]
My_List22.sort()
print (My_List22)


