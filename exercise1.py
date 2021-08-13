from os import read


my_file=open("exercise1.txt")
my_data=my_file.read()
print(my_data)
my_file.close()