#add import
import question_a
#Prints Header for Temperature Table
print("Celsius".rjust(8) + "Fahrenheit".rjust(12))
print('-' * 20)
#Prints from zero to 20
c = 0
while c <= 20:
    #Gets Function to convert Temperature
    f = question_a.get_fahrenheit(c)
    #Prints Table
    print(str(c).rjust(2) + str(f"{f:.1f}").rjust(12))
    c += 1
print(" ")









