# Group Assignement CSC 450 - Computer Networks
## Distance-vector algorithm

### Program overview
This program takes a network topology specified in a csv file and calculates the
distance vectors for each node in the specified network. The distance vector
estimates are calculated using the Bellman-Ford equation.

### Command Line Input
python dv_algorithm.py {topology_filename}

Note: the topology must be a comma seperated file with node names on the first
row anad first column. The cost of links between a row node and a column node
are the other cells

### Outputs
The output lines show the distance between the specified node and nodes x, y, z.

aaguillard@AA-VirtualBox:~/github/distancevector$ python3 dv_algorithm.py topology.csv
Distance vector for node x: 0 2 3
Distance vector for node y: 2 0 1
Distance vector for node z: 3 1 0

{Schoon put your output here, or maybe a screenshot}

### Python Version
The program is run using Python 3.
    Andre used Python 3.6
    Andrew used Python 3.6

### Member Responsibilities
Andre Aguillard formatted the output of the file and created the README.
Andrew Schoonmaker implemented the dv algorithm and the load topology functions.
