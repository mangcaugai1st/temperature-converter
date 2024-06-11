num = input("Type a number: ")
tempUnit = input("Choose an unit of temperature (F | C): ")
if tempUnit == 'F' or tempUnit == 'f':
    temp_unit_input = "°F"
    res = (5 * int(num) - 160) / 9;
    temp_unit_output = "°C"
elif tempUnit == 'C' or tempUnit == 'c':
    temp_unit_input = "°C"
    res = (9 * int(num )/ 5) + 32;
    temp_unit_output = "°F"
print("-------------------------------------")
print(f"\t{num}{temp_unit_input} = {res}{temp_unit_output}")
print("-------------------------------------")
print("       \\    ^__^")
print("        \\   (oo)\\_______")
print("            (__)\\       )\\/\\")
print("                ||----w |")
print("                ||     ||")