#python programming of using if,else,elif statement. 1 st question
#authore - nisha pagare
#date- 10/03/2021

#accepting the length from the user in cm
length_cm=float(input("Enter the length in cm:"))
    
if length_cm<0:
    print("The length entered by the user is invalid")
else:
    length_inches+(length_cm/2.54)
    print("the value of the length=",length_cm,"cm after converting into inches is",length_inches,"inches")
