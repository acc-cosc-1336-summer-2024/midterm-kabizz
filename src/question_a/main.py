#add import
import question_a

print("Celsius".rjust(8) + "Fahrenheit".rjust(12))
print('-' * 20)
c = 0
while c <= 20:
    f = question_a.get_fahrenheit(c)
    print(str(c).rjust(2) + str(f"{f:.1f}").rjust(12))
    c += 1
print(" ")









