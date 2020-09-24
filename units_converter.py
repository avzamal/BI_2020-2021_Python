# All values of the converter is in the keys of the dictionary
# and all values are in grams
unit_dict = {'Carat': 0.3,
             'Troy ounce': 31.1,
             'Centner': 100000,
             'Kilogram': 1001,
             'Gram': 1,
             'Dram': 1.77,
             'Tonne': 1000000,
             'Milligram': 0.001}

print("It is units converter. List of units in converter:")
for key in unit_dict:
    print(key, end="\n")
# User enters the units and the value
first_unit1 = input('Choose the unit you want to convert: \n')
second_unit2 = input('Choose the unit you want to convert to: \n')
print(first_unit1+' -> '+second_unit2)
convert_number = float(input('Enter the value:\n'))

# It is calculations
print(str(convert_number) + " " + first_unit1 + " -> " +
      str(convert_number*unit_dict[first_unit1]/unit_dict[second_unit2])
      + " " + second_unit2)
