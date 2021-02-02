"""

Name: Cameron Ball
FSUID: cbb18
Due Date: Wed, Jan 20, 2021
The program in this file is the individual work of Cameron Ball

"""

def isPalindrome(input):
    """
    Checks if a string is a palindrome
    """

    temp = ""                   # string to strip non-alpha characters
    reverse = ""                # to hold reverse of input

    for letter in input:        # for characters in input,
        if letter.isalpha():    # if char is alpha,
            temp += letter      # concatenate it to temp,
    lower = temp.lower()        # then convert non-alpha-stripped input to lowercase

    for letter in lower[::-1]:  # traverse characters of lower backwards, and
        reverse += letter       # add the letters. This produces a backwards copy of 'lower'

    return lower == reverse     # if input and its reverse are the same, it's a palindrome

print("Enter the strings:")

strings = []            # list of read-in strings
str = ""                # input string
while True:             # loop until user enters "Done"
    str = input()
    if str == "Done":
        break
    strings.append(str) # add input to list of strings

dictionary = {}         # output dictionary
counter = 1             # counter variable for keys
for x in strings:       # for each string input...
    if isPalindrome(x): # if it's a palindrome,
        dictionary["{}".format(counter)] = x # use counter as key, value as string
        counter += 1    # increment counter

print("The palindromes are:")
print(dictionary)
