#This program validates an input and then converts it into a twisted password with capitals and lowercases exchanged
ex=["!","@","#","$","{",",",".",]#Add as many characters as you wish
def validator():#Function to validate the input
    password=input("Ingrese la contraseña: ")
    condition=True
    cont=0
    for i in password:
        for j in ex:
            if (i==j):
                condition=False
                cont+=1
            else:
                cont+=1
    if (condition==True):
            print("Contraseña valida")
    else:
            print("Contraseña no valida")
    return condition, password

def converter(password):#Function to convert the input
    new_pass=""
    password=password[::-1]
    for i in password:
         if (i.isupper()):
            i=i.lower()
            new_pass=new_pass+i
         else:
            i=i.upper()
            new_pass=new_pass+i    
    print(new_pass)               

ret=validator()#Calling the function validator

if (ret[0]==True):
     converter(ret[1])#Calling the function converter with the validated
