import matplotlib.pyplot as plt

"""Graphing functions for data visualization
"""

def graph_speeds(speeds, unit='km/s'):
    plt.plot(speeds)
    plt.ylabel('speed ' + unit)
    plt.xlabel('observation')
    plt.show()