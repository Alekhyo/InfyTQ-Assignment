#DSA-Assgn-3
# Given two lists, both having integer elements, write a python program using python lists to create and return a new list as per the rule given below:
# If the double of an element in list1 is present in list2, then add it to the new list.



def check_double(list1,list2):
    new_list=[]
    for i in list1:
        if 2*i in list2:
            new_list.append(i)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))

#Input: list1=[11,8,23,7,25,15], list2=[6,33,50,31,46,78,16,34]
#output: new_list – [8,23,25]
