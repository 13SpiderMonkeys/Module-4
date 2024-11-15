import matplotlib.pyplot as plt

#generate cubic numbers
x_values_small = list(range(1,6)) #first 5 numbers
y_values_small = [x**3 for x in x_values_small]

x_values_large = list(range(1,5000))
y_values_large = [x**3 for x in x_values_large]

#plot the first 5 figures

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.scatter(x_values_small,y_values_small, c=y_values_small, cmap="viridis",s=100)
plt.title("First 5 Cubic Numbers")
plt.xlabel("Value")
plt.ylabel("Cubic Value")
plt.colorbar(label="Cubic Value")

#plot the first 5000 cubic numbers
plt.subplot(1,2,2)
plt.scatter(x_values_large,y_values_large, c=y_values_large, cmap="plasma",s=1)
plt.title("First 5000 Cubic Numbers")
plt.xlabel("Value")
plt.ylabel("Cubic Value")
plt.colorbar(label="Cubic Value")


#display plot
plt.tight_layout()
plt.savefig('Cubic_visual.svg')