# 6. Create a list of 5 numbers and find the largest among the list

def largest_in_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return max(l[0],largest_in_list(l[1:]))
l = [1,2,67,3,4,5]
print("The largest number in the list is:",largest_in_list
(l))