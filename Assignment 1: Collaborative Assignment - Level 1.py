#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    for i in range(0,max(len(list1),len(list2))):
        if list1[i]==None:
            merged_data=merged_data+' '+list2[-(i+1)]
        elif list2[-(i+1)]==None:
            merged_data=merged_data+' '+list1[i]
        else:
            merged_data=merged_data+' '+list1[i]+list2[-(i+1)]
    resultant_data=merged_data[1:]
    return resultant_data




#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)



#input: list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
#       list2=['y','tor','e','eps','ay',None,'le','n']

#output=“An apple a day keeps the doctor away”

