# ask user for a distance and target units (miles or km) and prints the conversion

# get distance and unit choice

print("Enter a distance")
distance = int(input())

print("Enter units to convert to - mi or km")
target_units = input()

if target_units == 'mi':
    origin_units = 'km'
    target_distance = distance / 1.6093
elif target_units == 'km':
    origin_units = 'mi'
    target_distance = distance * 1.6093
    
print(distance, origin_units, "equals", target_distance, target_units)