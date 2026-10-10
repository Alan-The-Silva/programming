# Create an empty set
s = set()

# Add elements in the set
s.add(1)
s.add(2)

# Set does not support duplication
s.add(3)
s.add(3)
print(s)

s.add(4)
s.add(5)
print(s)

# Removing elemets in the set
s.remove(4)
print(s)

print(f"The set has {len(s)} elements")