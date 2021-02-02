"""

Name: Cameron Ball
FSUID: cbb18
Due Date: Wed, Jan 20, 2021
The program in this file is the individual work of Cameron Ball

"""

def printTriangle(row):
    """
    printTriangle(row)

    Print Pascal's Triangle up to passed parameter value. Cannot print less than 3 rows.
    """

    ls = [ [1], [1, 1], [1, 2, 1] ] # initialise with first 3 rows of Pascal's Triangle

    # construct the triangle
    for x in range(3, row):                     # since ls is init'd with 0-2, start at 3
        r = []                                  # create list to be appended

        r.append( 1 )                           # each row begins with 1
        for y in range( 1, len( ls[-1] ) ):     # loop once more than the previous row's length
            r.append( ls[-1][y - 1] + ls[-1][y] )   # append sum of prev & current values from last list
        r.append( 1 )                           # each row ends with 1

        ls.append(r)                            # add the new list on the end

    # print the triangle
    for x in ls:
        for y in x:
            print(y, end = " ")
        print("\n", end = "")

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    printTriangle(n)
