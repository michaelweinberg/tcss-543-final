
from cProfile import label
import matplotlib.pyplot as plt

# function used to build the graphs
def plot(set):
    for result in set["results"]:
        for algorithm in set["results"][result]:
            x = algorithm["xAxis"]
            y = algorithm["values"]
            plt.plot(x, y, label=algorithm["name"])

        # naming the x axis
        plt.xlabel(set["xAxis"])
        # naming the y axis
        plt.ylabel(result)
        # giving a title to the graph
        plt.title(result + ' over ' + set["xAxis"] + ' for ' + set["dataset"])
        
        # show a legend on the plot
        plt.legend()
        
        # function to show the plot
        plt.show()