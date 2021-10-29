import os
from tempfile import TemporaryDirectory
import networkx as nx
import json
import sys
from source.nashFlowClass import NashFlow
import shutil

if __name__ == '__main__':
    tempDir = TemporaryDirectory()
    scipPath = shutil.which('scip')

    if scipPath is None:
        raise Exception("Path to scip executable could not be determined")

    data = json.load(sys.stdin)
    graph = nx.cytoscape_graph(data)

    if nx.is_directed(graph) is False:
        raise Exception("Input graph needs to be directed")

    if graph.graph["inflowRate"] <= 0:
        raise Exception("Inflow rate must be positive")

    nashFlow = NashFlow(
        graph,
        graph.graph["inflowRate"],
        -1,
        tempDir.name,
        os.path.join(os.path.dirname(__file__), 'source', 'templates', 'algorithm_1.zpl'),
        scipPath,
        True,
        0
    )

    nashFlow.run()
    flow_intervals = nashFlow.flowIntervals

    result = list(map(lambda x: {
        "start": x[0],
        "end": x[1],
        "labels": x[2].NTFNodeLabelDict
    }, flow_intervals))

    print(json.dumps(result))
