def is_in_range(value):
    return 0 <= value <= 100
print(is_in_range(50)) 

def count_case(s):
    uppercase = sum(1 for char in s if char.isupper())
    lowercase = sum(1 for char in s if char.islower())
    return uppercase, lowercase


result = count_case("Hello World!")
print("Uppercase:", result[0], "Lowercase:", result[1]) 

name = input("Enter your name: ").strip()
formatted_name = name.capitalize()
print(f"Hello, {formatted_name}!")

def remove_last_char(s):
    return s[:-1] if len(s) > 1 else s


print(remove_last_char("Hello!")) 
print(remove_last_char("t"))     
print(remove_last_char(""))        

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print(celsius_to_fahrenheit(0))    
print(fahrenheit_to_celsius(32))  

temp = input("Enter a temperature (e.g., 25C): ").strip().upper()
if temp.endswith("C"):
    c = float(temp[:-1])
    f = celsius_to_fahrenheit(c)
    print(f"{c}C = {f:.2f}F")
elif temp.endswith("F"):
    f = float(temp[:-1])
    c = fahrenheit_to_celsius(f)
    print(f"{f}F = {c:.2f}C")
else:
    print("Invalid format. Use a number followed by 'C' or 'F'.")

temps = []
for _ in range(6):
    temp = input("Enter a temperature (e.g., 25C): ").strip().upper()
    if temp.endswith("C"):
        temps.append(float(temp[:-1]))
    else:
        print("Invalid input. Must end with 'C'.")

if temps:
    print("Max:", max(temps), "C")
    print("Min:", min(temps), "C")
    print("Mean:", sum(temps) / len(temps), "C")

temps = []
while True:
    temp = input("Enter a temperature (press Enter to stop): ").strip().upper()
    if not temp:
        break
    if temp.endswith("C"):
        temps.append(float(temp[:-1]))
    else:
        print("Invalid input. Must end with 'C'.")

if temps:
    print("Max:", max(temps), "C")
    print("Min:", min(temps), "C")
    print("Mean:", sum(temps) / len(temps), "C")
else:
    print("Thank you.")  
    

