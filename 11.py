# 11. write a function to extract the third string stored in a list and the print its length.

def extract_string(l):
    return len(l[2])
l = ["Vipin", "Kumar", "Python", "Java", "C++"]
print("The length of the third string in the list is:", extract_string(l))