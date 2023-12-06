import time
import plot
import tracemalloc
from scaling_ff import scaling_ff
from read_graph import read_graph

algorithms = { 
    "scaling-ff": scaling_ff,
    "test-ff": scaling_ff,
}
graphTypes = ["bipartite", "fixedDegree"]
# Bipartite graph
n = [25, 50]
data = []

for graphType in graphTypes:
    timeResults = []
    memoryResults = []
    for algo in algorithms:
        elapsedTimes = []
        memoryUsage = []
        algorithm = algorithms[algo]
        for x in n:
            file_name = f"./test-graphs/{graphType}/{graphType}"+str(x)+".txt"
            graph,nodes = read_graph(file_name)
            tracemalloc.start()
            startTime = time.time()
            max_flow = algorithm(graph, nodes)
            endTime = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            timeElapsed = (endTime - startTime)*1000 # to get milliseconds
            elapsedTimes.append(timeElapsed)
            memoryUsage.append(peak)
            print("Max Flow: ", max_flow)
        timeResults.append({"name": algo, "values": elapsedTimes, "xAxis": n})
        memoryResults.append({"name": algo, "values": memoryUsage, "xAxis": n})
    data.append({"dataset": f"{graphType.capitalize()} Graph", "xAxis": 'size', "results": {"time": timeResults, "memory": memoryResults}})

for set in data:
    plot.plot(set)