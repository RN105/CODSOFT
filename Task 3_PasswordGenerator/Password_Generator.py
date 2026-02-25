import random
import string

print(f"------------- P A S S W O R D   G E N E R A T O R -----------------")
print(f"********************************************************************")

length_ofpass = int(input(f" Enter the desire lenght of the password =  "))

character = string.ascii_letters + string.digits + string.punctuation   

password = "" 
for i in range(length_ofpass): 
    password += random.choice(character)  
                                        
print(f" YOUR PASSWORD IS = {password}")