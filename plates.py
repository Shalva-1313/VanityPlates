def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

#CHECKS THAT FIRST TWO VALUES ARE LETTERS AND NOT NUMBERS
    for r in s:
        if s[0:2].isalpha() == False:
            return False

#checks that it is between 2-6 characters and that there are no special characters
    for r in s:
      if len(s) < 2 or len(s) > 6 or s.isalnum() == False:
        return False

# Checks if the first number is a zero or not (it should not be)
    holder = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            holder += s[i]
            if holder[0] == "0":
                return False

#checks for all characters which returns True
    if s.isalpha():
        return True

#checks for no letter after number
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            holder = i
            break

    valid = True
    for i in range(holder, len(s)):
        if s[i].isalpha():
            valid = False

    if valid == False:
        return False
    return True

if __name__ == "__main__":
    main()
