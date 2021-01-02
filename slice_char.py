"""Given a string,S of length N that is indexed from 0 to N-1, 
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line

Note 0 is considered to be an even index.

input format
The first line contains an integer, T (the number of test cases).
Each line i of the T subsequent lines contain a string, S.
"""

#for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])

#slicing list x[startAt:endBefore:step]

#* unpacks container data types like lists, sets, etc. and prints every member at once in order, with whatever separator you set.
#so far only available for print function on list or tuple

#x = "#".join(myTuple) join function
#output John#Peter#Vicky

def slice_char(st):
     print(st[::2], st[1::2])    
    
if __name__ == '__main__':
    n= int(input())  
    #result of input is not a list. there is no raw_input for py3
    #need multiple input call
    for i in range(n):
        slice_char(input())
    
