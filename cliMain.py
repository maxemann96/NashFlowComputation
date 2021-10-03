if __name__ == '__main__':
    import networkx as nx
    import json
    import sys
    from source.nashFlowClass import NashFlow

    data = json.load(sys.stdin)
    graph = nx.cytoscape_graph(data)
    nashFlow = NashFlow(
        graph,
        1,
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
        "labels": x[2].NTFNodeLabelDict
    }, flow_intervals))

    print(json.dumps(result))

    # result.
    # result = nx.cytoscape_data(nashFlow.network)
    # print(json.dumps(result))*/
