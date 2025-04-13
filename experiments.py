import datetime
import os

import matplotlib.pyplot as plt
import numpy as np
from graph import Graph
from tsp import tsp_alg
import time

i_start = 20
i_end = 400
i_delta = 10
repeat_amount = 10
density = 0.2 # 0-1

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
results = []
average_times = []
i = i_start

results.append(f"Experiment: {timestamp}")
results.append(f"Density: {density}")
results.append(f"Vertexes: {i_start} - {i_end}, delta: {i_delta}")
results.append(f"Same vertex amount repeat times: {repeat_amount}")
results.append("")


while i <= i_end:
    results.append(f"{i} vertexes:")
    sum = 0
    for j in range(repeat_amount):
        graph = Graph(i)
        graph.generate_random_graph(density=density, weight_range=(1, 6))
        start_time = time.perf_counter()
        (path, total) = tsp_alg(graph)
        elapsed_time = (time.perf_counter() - start_time)*1000
        results.append(f"Attempt {j+1}: {elapsed_time}ms")
        sum += elapsed_time
    average = sum/repeat_amount
    results.append(f"Average time: {average}ms")
    average_times.append(average)
    i+=i_delta


os.makedirs(f"ExperimentsResults/Experiment_{timestamp}", exist_ok=True)
with open(f"ExperimentsResults/Experiment_{timestamp}/full_results.txt", "w") as f:
    for result in results:
        f.write(result + "\n")


# Sample experimental data
x = np.arange(i_start, i_end+1, i_delta)  # X-axis data: experiment iterations or time
y = np.sin(x)             # Y-axis data: a sample outcome, e.g., sensor reading or computed value

# Create the figure and adjust its size for clarity
plt.figure(figsize=(8, 6), dpi=200)

# Plotting the data; use markers and lines to highlight the experimental trend
plt.plot(x, average_times, marker='o', linestyle='-', color='b', label=f"TSP time consumption\nDensity={density}", )

# Adding descriptive elements for better understanding
plt.title("Experiment Results: TSP time consumption depending on density and vertex amount")
plt.xlabel("Vertex amount")
plt.ylabel("Time, ms")
plt.legend()
plt.grid(True)

# Display the plot
plt.savefig(f"ExperimentsResults/Experiment_{timestamp}/diagram.png", dpi=200)
plt.show()

