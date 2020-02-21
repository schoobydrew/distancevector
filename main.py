# Andrew Schoonmaker and Andre Aguillard
# Dijkstra algorithm in python 3
#!/usr/bin/env python3
import argparse
# load_topology
# parameters: string filepath to csv
# returns: data frame of weights
# data frame -> dictionary of nodes where key is node name and value is dictionary of weights
# dictionary of weights -> dictionary of weights for paths where key is node name
def load_topology(filepath):
    f = open(filepath)
    data = f.read().splitlines()
    f.close()
    frame = {}
    nodes = data[0][1:].split(',')
    for d in data[1:]:
        row = d.split(',')
        node = row[0]
        weights = row[1:]
        frame[node] = {n:int(w) for n,w in zip(nodes,weights)}
    return frame
if __name__ == "__main__":
    # arg parser
    ap = argparse.ArgumentParser()
    ap.add_argument("filepath", type=str)
    # dictionary of arguments
    args = vars(ap.parse_args())
    # load in topology from command line
    data_frame = load_topology(args["filepath"])
