import pandas as pd
import matplotlib.pyplot as plt

# Load just the two columns (header doesn't match so by column number)
df = pd.read_csv("datad.csv", usecols=[14, 21], header=0,
                 names=["viol_level", "city"])

# Keep valid severity values and the 8 most common cities
df = df[df["viol_level"].isin(["*", "**", "***"])]
df["city"] = df["city"].str.strip().str.upper()
df = df[df["city"].isin(df["city"].value_counts().head(8).index)]

# gets the percentages of each violation level by city
table = pd.crosstab(df["city"], df["viol_level"], normalize="index") * 100

# Draw the heat map
fig, ax = plt.subplots()
im = ax.imshow(table, cmap="YlOrRd")
ax.set_xticks(range(len(table.columns)), table.columns)
ax.set_yticks(range(len(table.index)), table.index)
ax.set_xlabel("Violation level")
ax.set_ylabel("City")
ax.set_title("Violation level by city (%)")
fig.colorbar(im)

# Print the number in each cell
for i in range(table.shape[0]):
    for j in range(table.shape[1]):
        ax.text(j, i, f"{table.iloc[i, j]:.0f}", ha="center", va="center")

plt.show()