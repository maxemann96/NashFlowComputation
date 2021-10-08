import os
from tempfile import TemporaryDirectory
import networkx as nx
import json
import sys
from source.nashFlowClass import NashFlow

if __name__ == '__main__':
    tempDir = TemporaryDirectory()

    data = json.load(sys.stdin)
    graph = nx.cytoscape_graph(data)
    nashFlow = NashFlow(
        graph,
        1,
        -1,
        tempDir.name,
        os.path.join(os.getcwd(), 'source', 'templates', 'algorithm_1.zpl'),
        "/usr/bin/scip",
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
