# All values of the converter is in the keys of the dictionary
# and all values are in grams
unit_dict = {'Pound': 453.59,
             'Ounce': 28.35,
             'Carat': 0.2,
             'Kilogram': 1000,
             'Gram': 1,
             'Tonne': 1000000,
             'Milligram': 0.001,
             'Troy ounce': 31.1,
             'Centner': 100000,
             'Dram': 1.77,
             'Grain': 0.0648}

print("It is units converter. List of units in converter:")
for key in unit_dict:
    print(key, end="\n")
# User enters the units and the value
first_unit1 = input('Choose the unit you want to convert: \n')
second_unit2 = input('Choose the unit you want to convert to: \n')
print(first_unit1+' -> '+second_unit2)
convert_number = float(input('Enter the number:\n'))

# Here is calculations
print(str(convert_number) + " " + first_unit1 + " -> " +
      str(convert_number*unit_dict[first_unit1]/unit_dict[second_unit2])
      + " " + second_unit2)
