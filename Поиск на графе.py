graph = {'start': {'a': 2, 'b': 3},
         'a': {'c': 3, 'd': 2, 'b': 2},
         'b': {'g': 4},
         'c': {'d': 3},
         'd': {'e': 1, 'g': 1},
         'e': {'finish': 4},
         'g': {'e': 2, 'finish': 1},
         'finish': {}
         }

inf = float('inf')
costs = {'a': 2, 'b': 3, 'c': inf, 'd': inf,
         'e': inf, 'g': inf, 'finish': inf}

parents = {'a': 'start', 'b': 'start', 'finish': None}

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)


def print_graph(p):
    current_key = 'finish'
    path = [current_key]

    for i in parents:
        path.append(parents[current_key])
        current_key = parents[current_key]

    print(path[::-1])


while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

first_node = 'finish'
print(costs)
print(parents)
print_graph(parents)
