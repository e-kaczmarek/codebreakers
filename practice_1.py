x = 3
flavors = ['cherry', 'orange', 'vanilla']
identity = ['Unknown Alias', 25, False]
owns_a_dog = True
fbi = "Federal Bureau of Investigation"

print(type(x))
print(type(flavors))
print(type(identity))
print(type(owns_a_dog))
print(type(fbi))

x = float(x)
print(x)

print(fbi[8])
print(fbi[:7])
print(fbi[-16:-14])

print(flavors[:2])
print(flavors[2])
owns_a_dog = False
identity[0] = 'some name'
print(identity)
print(flavors[::-1])
identity[1] = x
print(identity)
print(flavors[0][2])
print(len(fbi))
print("This gelato store only has", x, 'flavors!')
print(flavors[::2])
print([flavors[0]] + [flavors[2]])
print(flavors[0] in identity)
print(False in identity)
print(x in identity)
