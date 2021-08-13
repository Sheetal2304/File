#Aapke paas ek list hai. Iss list mein har string
#ko ek file-question3.txt naam ki file mein nayi 
#line mein daalo. Aapki list yeh rahi:

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
my_file=open("exercise3.txt","a")
for i in banks_list:
    # print(i)
    my_file.write(i)
    my_file.write("\n")
my_file.close()
# print(my_file)

