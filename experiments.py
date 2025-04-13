import datetime
import os

import matplotlib.pyplot as plt
import numpy as np
from graph import Graph
from tsp import tsp_alg
import time

vertex_start = 20
vertex_end = 400
vertex_step = 10
repeat_amount = 10
density = 1 # 0-1

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
results = []
average_times = []
i = vertex_start

results.append(f"Experiment: {timestamp}")
results.append(f"Density: {density}")
results.append(f"Vertexes: {vertex_start} - {vertex_end}, delta: {vertex_step}")
results.append(f"Same vertex amount repeat times: {repeat_amount}")
results.append("")


while i <= vertex_end:
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
    i+=vertex_step


os.makedirs(f"ExperimentsResults/Experiment_{timestamp}", exist_ok=True)
with open(f"ExperimentsResults/Experiment_{timestamp}/full_results.txt", "w") as f:
    for result in results:
        f.write(result + "\n")


x = np.arange(vertex_start, vertex_end + 1, vertex_step)
y = np.sin(x)

plt.figure(figsize=(8, 6), dpi=200)

plt.plot(x, average_times, marker='o', linestyle='-', color='b', label=f"TSP time consumption\nDensity={density}", )

plt.title("Experiment Results: TSP time consumption depending on density and vertex amount")
plt.xlabel("Vertex amount")
plt.ylabel("Time, ms")
plt.legend()
plt.grid(True)

plt.savefig(f"ExperimentsResults/Experiment_{timestamp}/diagram.png", dpi=200)
plt.show()

