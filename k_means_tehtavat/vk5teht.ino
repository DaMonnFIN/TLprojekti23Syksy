import numpy as np
import pandas as pd

# Read the data from the file
data = pd.read_csv('/C:/Projekti23S/TLprojekti23Syksy/k_means_tehtavat/vk5teht.ino', delimiter=' ')

# Count the number of [x, y, z] triplets
numberOfRows = len(data)

# Print the result
print("Number of [x, y, z] triplets:", numberOfRows)
