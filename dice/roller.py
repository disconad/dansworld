import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Generate 1000 samples of rolling 4 six-sided dice and keeping the highest 3 values
dice_rolls = np.random.randint(1, 7, size=(1000, 4))

# Sort the dice rolls along the last axis (axis=1) to get the highest three values
dice_rolls_sorted = np.sort(dice_rolls, axis=1)

# Sum the three highest dice values for each sample
data = np.sum(dice_rolls_sorted[:, 1:], axis=1)

# Count occurrences of each value
counts = np.bincount(data)

# Plotting
fig, ax = plt.subplots(figsize=(8, 4), facecolor='w')

# Define colors
top = plt.get_cmap('Oranges', 128)
bottom = plt.get_cmap('Blues', 128)
newcolors = np.vstack((top(np.linspace(0, 1, 128)), bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='OrangeBlue')

# Create bars
bars = ax.bar(range(3, 19), counts[3:19], color=newcmp(counts[3:19] / max(counts[3:19])))

# Set x-ticks to integers
plt.xticks(range(3, 19))

plt.show()
