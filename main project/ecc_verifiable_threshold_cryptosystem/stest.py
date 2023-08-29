import cv2
import string
import os

def encrypts():
    d={}
    c={}



    for i in range(255):
        d[chr(i)]=i
        c[i]=chr(i)
    
    
    #print(c)

    x=cv2.imread("D:/VIT/F1- CSE3502 - Information Security Management/Digital Assignment/ISM LAB/project/ecc_verifiable_threshold_cryptosystem/2.jpg")

    i=x.shape[0]
    j=x.shape[1]
    # print(i,j)

    key=input("Enter key to edit(Security Key) : ")
    skey = key
    # text=input("Enter text to hide : ")


    # Open the file for reading
    with open('D:/VIT/F1- CSE3502 - Information Security Management/Digital Assignment/ISM LAB/project/ecc_verifiable_threshold_cryptosystem/data/secret.txt', 'r') as f:
        file_contents = f.read()
    strings_list = file_contents.split(',')
    # print(strings_list)
    strings_list = [s.strip() for s in strings_list]

    kl=0
    tln=4
    z=0 #decides plane
    n=0 #number of row
    m=0 #number of column

    for j in range(len(strings_list)):
        length = len(strings_list[j])
        # print(length)
        for i in range(length):
            x[n,m,z]=d[strings_list[j][i]]^d[key[kl]]
            n=n+1
            m=m+1
            m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                        #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
            kl=(kl+1)%len(key)
        s = "person_"+str(j+1)+".jpg"
        cv2.imwrite(s,x) 
        os.startfile(s)

    print("Public and Private key incorporated image successfully created.")    



    # l=len(text)
    # for i in range(l):
    #     x[n,m,z]=d[text[i]]^d[key[kl]]
    #     n=n+1
    #     m=m+1
    #     m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
    #                 #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
    #     kl=(kl+1)%len(key)

    # s = "dolo"+str(1)+".jpg"
        
    # cv2.imwrite(s,x) 
    # os.startfile(s)
    # print("Data Hiding in Image completed successfully.")
    # #x=cv2.imread(“encrypted_img.jpg")
    def decrypts():
        kl=0
        z=0 #decides plane
        n=0 #number of row
        m=0 #number of column

        ch = int(input("\nEnter 1 to extract data from Image : "))
        for j in range(len(strings_list)):
            tln=len(strings_list[j])
            q = "D:/VIT/F1- CSE3502 - Information Security Management/Digital Assignment/ISM LAB/project/person_"+str(j+1)+".jpg"
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


