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

    if nx.is_multigraphical(graph) is True:
        raise Exception("Input graph needs to be not a multigraph")

    if nx.is_directed(graph) is False:
        raise Exception("Input graph needs to be directed")

    if graph.graph["inflowRate"] <= 0:
        raise Exception("Inflow rate must be positive")

    nashFlow = NashFlow(
        graph,
        graph.graph["inflowRate"],
        graph.graph["maximumNumberOfIntervals"],
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
        "nodeLabels": x[2].NTFNodeLabelDict,
        "edgeFlow": list(map(lambda y: {
            "source": y[0],
            "target": y[1],
            "flow": x[2].NTFEdgeFlowDict[y]
        }, x[2].NTFEdgeFlowDict))
    }, flow_intervals))

    print(json.dumps(result))
