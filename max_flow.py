import sys
import time
import tracemalloc
from scaling_ff import scaling_ff
from read_graph import read_graph
from ff import ff
from preflow_push import preflow_push

algorithms = { 
    "ff": ff,
    "scaling-ff": scaling_ff,
    "preflow_push": preflow_push
}

if len(sys.argv) == 1 or sys.argv[1] == '--benchmark':
    import plot
    graphTypes = ["bipartite", "fixedDegree"]
    n = [25, 50, 100, 200]
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
else:
    for file_name in sys.argv[1:]:
        print(file_name)
        for algo in algorithms:
            graph,nodes = read_graph(file_name, algo)
            tracemalloc.start()
            startTime = time.time()
            max_flow = algorithms[algo](graph, nodes)
            endTime = time.time()
            timeElapsed = (endTime - startTime)*1000
            print(f"\t{algo}: Max Flow is {max_flow}\tTime elapsed is {timeElapsed}\tMemory usage is {tracemalloc.get_traced_memory()[1]}")
            tracemalloc.stop()


