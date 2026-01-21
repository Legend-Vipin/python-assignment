# 9. Create a string and print the characters from 5th to 10 in direct and reverse order.

def print_characters():
    string = "VipinKumar"
    print(f"String: {string}")
    print(f"Characters from 5th to 10 in direct order: {string[4:10]}")
    print(f"Characters from 5th to 10 in reverse order: {string[9:3:-1]}")

if __name__ == "__main__":
    print_characters()