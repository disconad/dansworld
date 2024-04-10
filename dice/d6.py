import numpy as np
import matplotlib.pyplot as plt

# Roll a six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000000000)

# Calculate the counts of each roll
counts = np.bincount(rolls)[1:]

# Calculate the total count and percentage change from the top result
total_count = np.sum(counts)
percentage_change = ((counts - counts.max()) / counts.max()) * 100

# Plotting the bar graph
plt.figure(figsize=(8, 4))
plt.bar(range(1, 7), counts, color='skyblue')
plt.xlabel('Roll Result')
plt.ylabel('Frequency')
plt.title('Roll Results Distribution')
plt.xticks(range(1, 7))

plt.show()

# Display the table with total counts and percentage change
print("Roll\tCount\t% Change from Top")
for roll, count, percent in zip(range(1, 7), counts, percentage_change):
    print(f"{roll}\t{count}\t{percent:.2f}%")
print(f"Total\t{total_count}\t-")
