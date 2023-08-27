import cv2
import string
import os
from stest import skey
from stest import c
from stest import d
from stest import x

kl=0
z=0 #decides plane
n=0 #number of row
m=0 #number of column

ch = int(input("\nEnter 1 to extract data from Image : "))
for j in range(len(strings_list)):
    tln=len(strings_list[j])
    q = "C:/Users/HARSHIL/Desktop/ISM LAB/project/person_"+str(j+1)+".jpg"
    y =cv2.imread(q)
    if ch == 1:
        key1=input("\n\nRe enter skey to extract text : ")
        decrypt=""

        if skey == key1 :
            for i in range(len(strings_list[j])):
                decrypt+=c[x[n,m,z]^d[skey[kl]]]
                n=n+1
                m=m+1
                m=(m+1)%3
                kl=(kl+1)%len(skey)
            print("Encrypted text was : ",decrypt)
        else:
            print("skey doesn't matched.")
    else:
        print("Thank you. EXITING.")