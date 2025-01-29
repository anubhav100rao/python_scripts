import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate a simple random walk
np.random.seed(42)
n_steps = 1000
steps = np.random.choice([-1, 1], size=n_steps)  # Random steps +1 or -1
random_walk = np.cumsum(steps)  # Cumulative sum to simulate position

# Create a pandas Series to handle and plot
time_series = pd.Series(random_walk)
time_series.plot(title="Simple Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()
