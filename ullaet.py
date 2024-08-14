import numpy as np

# Example input arrays
ea = [np.pi / 4, np.pi / 6]  # Example angles in radians
xyz = [0, 0, 0]  # Initialize xyz array with zeros

# Perform the calculation and assignment
xyz[2] = np.cos(ea[0]) * np.cos(ea[1])

# Print the result
print(xyz)  # Output will be: [0, 0, 0.6123724356957946]
