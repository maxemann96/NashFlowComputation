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

    nodeList = [n for n in [node['data']['id'] for node in data['elements']['nodes']] if n != 's' and n != 't']
    nodeMap = {el: str(idx) for idx, el in enumerate(nodeList)}

    nodeMap['s'] = 's'
    nodeMap['t'] = 't'

    for node in data['elements']['nodes']:
        node['data']['id'] = nodeMap[node['data']['id']]
        node['data']['name'] = node['data']['id']
        node['data']['value'] = node['data']['id']
        node['data']['label'] = node['data']['id']

    for edge in data['elements']['edges']:
        edge['data']['source'] = nodeMap[edge['data']['source']]
        edge['data']['target'] = nodeMap[edge['data']['target']]

    # print(json.dumps(data), file=sys.stderr)

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

    nodeReverseMap = {v: k for k, v in nodeMap.items()}

    result = list(map(lambda x: {
        "start": x[0],
        "end": x[1],
        "nodeLabels": {nodeReverseMap[k]: v for k, v in x[2].NTFNodeLabelDict.items()},
        "edgeFlow": list(map(lambda y: {
            "source": nodeReverseMap[y[0]],
            "target": nodeReverseMap[y[1]],
            "flow": x[2].NTFEdgeFlowDict[y]
        }, x[2].NTFEdgeFlowDict))
    }, flow_intervals))

    print(json.dumps(result))
