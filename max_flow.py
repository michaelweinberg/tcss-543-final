import time
import plot
import tracemalloc
from scaling_ff import scaling_ff
from read_graph import read_graph
from ff import ff
from preflow_push import preflow_push

algorithms = { 
    # "ff": ff,
    # "scaling-ff": scaling_ff,
    "preflow_push": preflow_push
}
# graphTypes = ["Bipartite", "FixedDegree"]
graphTypes = ["Bipartite"]
n = [25, 50, 75, 100]
data = []

for graphType in graphTypes:
    timeResults = []
    memoryResults = []
    for algo in algorithms:
        elapsedTimes = []
        memoryUsage = []
        algorithm = algorithms[algo]
        for x in n:
            file_name = f"./test-graphs/{graphType}/{graphType}"+str(x)+"-10-percent.txt"
            graph,nodes = read_graph(file_name, algo)
            tracemalloc.start()
            startTime = time.time()
            max_flow = algorithm(graph, nodes)
            endTime = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            timeElapsed = (endTime - startTime)*1000 # to get milliseconds
            elapsedTimes.append(timeElapsed)
            memoryUsage.append(peak)
            print(f"Max Flow of {graphType}{x} calculated by {algo}: ", max_flow)
        timeResults.append({"name": algo, "values": elapsedTimes, "xAxis": n})
        memoryResults.append({"name": algo, "values": memoryUsage, "xAxis": n})

    data.append({"dataset": f"{graphType} Graph", "xAxis": 'size', "results": {"time": timeResults, "memory": memoryResults}})

for set in data:
    plot.plot(set)