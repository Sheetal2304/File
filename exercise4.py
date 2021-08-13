my_file=open("exercise4.txt","r")
# my_data=my_file.read()
for i in my_file:
    # print(i)
    if "shimla" in i:
        shimla=open("shimla.txt","a")
        shimla.write(i)
    elif "delhi" in i:
        delhi=open("delihi.txt","a")
        delhi.write(i)
    else:
        other=open("other.txt","a")
        other.write(i)
        