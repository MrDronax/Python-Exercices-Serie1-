name=input("Entrez votre nom: ")
age=int(input("Entrez votre age: "))
repeat=int(input("Entrez nombre de repetition: "))

s=name+" will be 100 years old in: "+str(2018+(100-age))+"\n"
print(repeat * s)

#Method 2:
#for x in range(repeat):
#   print("you will be 100 years old in the year "+str(tmp))
