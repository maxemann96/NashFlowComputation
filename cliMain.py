if __name__ == '__main__':
    import networkx as nx
    import json
    from source.nashFlowClass import NashFlow

    rawData = """{
  "data": {
    "flows": [
      {
        "startAt": 0,
        "flow_total": 5,
        "flow_per_time_unit": 1,
        "path": ["s", "v3", "v2", "t"]
      },
      {
        "startAt": 0,
        "flow_total": 1,
        "flow_per_time_unit": 1,
        "path": ["s", "v1", "v2", "v3", "v4", "t"]
      }
    ]
  },
  "directed": true,
  "multigraph": false,
  "elements": {
    "nodes": [
      {
        "data": {
          "label": "s",
          "id": "s",
          "value": "s",
          "position": [0, 0]
        }
      },
      {
        "data": {
          "label": "v1",
          "id": "v1",
          "value": "v1",
          "position": [0, 0]
        }
      },
      {
        "data": {
          "label": "v2",
          "id": "v2",
          "value": "v2",
          "position": [0, 0]
        }
      },
      {
        "data": {
          "label": "v3",
          "id": "v3",
          "value": "v3",
          "position": [0, 0]
        }
      },
      {
        "data": {
          "label": "v4",
          "id": "v4",
          "value": "v4",
          "position": [0, 0]
        }
      },
      {
        "data": {
          "label": "t",
          "id": "t",
          "value": "t",
          "position": [0, 0]
        }
      }
    ],
    "edges": [
      {
        "data": {
          "transitTime": 3,
          "outCapacity": 1,
          "source": "s",
          "target": "v1"
        }
      },
      {
        "data": {
          "transitTime": 2,
          "outCapacity": 1,
          "source": "s",
          "target": "v3"
        }
      },
      {
        "data": {
          "transitTime": 2,
          "outCapacity": 1,
          "source": "v3",
          "target": "v2"
        }
      },
      {
        "data": {
          "transitTime": 3,
          "outCapacity": 1,
          "source": "v3",
          "target": "v4"
        }
      },
      {
        "data": {
          "transitTime": 3,
          "outCapacity": 1,
          "source": "v1",
          "target": "v2"
        }
      },
      {
        "data": {
          "transitTime": 3,
          "outCapacity": 1,
          "source": "v4",
          "target": "t"
        }
      },
      {
        "data": {
          "transitTime": 2,
          "outCapacity": 1,
          "source": "v2",
          "target": "t"
        }
      }
    ]
  }
}"""

    data = json.loads(rawData)
    graph = nx.cytoscape_graph(data)
    nashFlow = NashFlow(
        graph,
        2,
        -1,
        "/Users/maximilian/TEST",
        "/Users/maximilian/IdeaProjects/NashFlowComputation/source/templates/algorithm_1.zpl",
        "/usr/local/bin/scip",
        True,
        0
    )

    nashFlow.run()

    result = nx.cytoscape_data(nashFlow.network)

    print("Hello world!")
