# All values of the converter is in the keys of the list
# and all values are in grams
unit_list = {'Pound': 453.59,
             'Ounce': 28.35,
             'Carat': 0.2,
             'Troy ounce': 31.1,
             'Centner': 100000,
             'Kilogram': 1000,
             'Gram': 1,
             'Dram': 1.77,
             'Tonne': 1000000,
             'Milligram': 0.001}

print("It is units converter. List of units in converter:")
for key in unit_list:
    print(key, end="\n")
# User enters the units and the value
first_unit = input('Choose the unit you want to convert: \n')
second_unit = input('Choose the unit you want to convert to: \n')
print(first_unit+' -> '+second_unit)
convert_number = float(input('Enter the number:\n'))

# Here is calculations
after_conversion = convert_number*unit_list[first_unit]/unit_list[second_unit]

print(str(convert_number) + " " + first_unit + " -> " + str(after_conversion)
      + " " + second_unit)
