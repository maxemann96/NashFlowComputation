import copy


def transform(data):
    data = copy.deepcopy(data)

    node_list = [n for n in [node['data']['id'] for node in data['elements']['nodes']] if n != 's' and n != 't']
    node_map = {el: str(idx) for idx, el in enumerate(node_list)}

    node_map['s'] = 's'
    node_map['t'] = 't'

    for node in data['elements']['nodes']:
        node['data']['id'] = node_map[node['data']['id']]
        node['data']['name'] = node['data']['id']
        node['data']['value'] = node['data']['id']
        node['data']['label'] = node['data']['id']

    for edge in data['elements']['edges']:
        edge['data']['source'] = node_map[edge['data']['source']]
        edge['data']['target'] = node_map[edge['data']['target']]

    return data, node_map
