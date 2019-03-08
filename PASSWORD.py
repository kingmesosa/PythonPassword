import re # imports regular expression
def password():
        pw = input("Enter a password: ")
        if len(pw) > 16:
            print("Has to be between 6 and 16 characters")
        elif len(pw) < 6:
            print("Has to be between 6 and 16 characters")
        elif re.search('[0-9]', pw) is None:
            print("Password must have a number in it.")
        elif re.search('[a-z]', pw) is None:
            print("Password must have a lowercase character in it.")
        elif re.search('[A-Z]', pw) is None:
            print("Password must have capital character in it.")
        elif re.search("[^a-zA-Z0-9]+", pw) is None:
            print("Password must have special character in it.")
        else:
            print("Thanks for setting password")
password()