if __name__ == '__main__':
    import networkx as nx
    import json
    import sys
    from source.nashFlowClass import NashFlow

    data = json.load(sys.stdin)
    graph = nx.cytoscape_graph(data)
    nashFlow = NashFlow(
        graph,
        2,
        -1,
        "/Users/maximilian/TEST",
        "/Users/maximilian/Development/NashFlowComputation/source/templates/algorithm_1.zpl",
        "/usr/local/bin/scip",
        True,
        0
    )

    nashFlow.run()
    flow_intervals = nashFlow.flowIntervals

    result = list(map(lambda x: {
        "start": x[0],
        "end": x[1],
        "flow": list(map(lambda y: {
            "source": y[0],
            "target": y[1],
            "flow": x[2].NTFEdgeFlowDict[y]
        }, x[2].NTFEdgeFlowDict))
    }, flow_intervals))

    print(json.dumps(result))

    # result.
    # result = nx.cytoscape_data(nashFlow.network)
    # print(json.dumps(result))*/
