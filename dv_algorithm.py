# Andrew Schoonmaker and André Aguillard
# Distance vector algorithm in python 3
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
# distance_vector
# parameters: data frame of topology
# returns: data frame of updated topology and paths
def distance_vector(topology):
    # initialize distance vector updated topology
    dv = {}
    # iterate through nodes
    for node in topology:
        dv[node] = {n:{"cost":c, "path":node+n} for n,c in topology[node].items()}
    # make multiple passes
    for i in range(len(dv)-1):
        # iterate through nodes
        for node in dv:
            # iterate through targets
            for d in dv[node]:
                # compare target cost to other reported costs
                for n in dv:
                    if (dv[node][d]["cost"] > dv[node][n]["cost"] + dv[n][d]["cost"]):
                        dv[node][d]["cost"] = dv[node][n]["cost"] + dv[n][d]["cost"]
                        dv[node][d]["path"] = dv[node][n]["path"] + dv[n][d]["path"]
    return dv
if __name__ == "__main__":
    # arg parser
    ap = argparse.ArgumentParser()
    ap.add_argument("filepath", type=str)
    # dictionary of arguments
    args = vars(ap.parse_args())
    # load in topology from command line
    data_frame = load_topology(args["filepath"])
    dv_frame = distance_vector(data_frame)
    # Format the output and print to standard out
    # reference the source below for accessing nested dictionaries
    # source: https://www.learnbyexample.org/python-nested-dictionary/
    print("Distance vector for node x: {} {} {}".format(dv_frame['x']['x']['cost'],dv_frame['x']['y']['cost'],dv_frame['x']['z']['cost']))
    print("Distance vector for node y: {} {} {}".format(dv_frame['y']['x']['cost'],dv_frame['y']['y']['cost'],dv_frame['y']['z']['cost']))
    print("Distance vector for node z: {} {} {}".format(dv_frame['z']['x']['cost'],dv_frame['z']['y']['cost'],dv_frame['z']['z']['cost']))
