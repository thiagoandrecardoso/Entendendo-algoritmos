graph = {
    "begin": {"a": 6, "b": 2},
    "a": {"end": 1},
    "b": {"a": 3, "end": 5},
    "end": {}
}
infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "end": infinity
}
parents = {
    "a": "begin",
    "b": "begin",
    "end": None
}
processed = []


def find_lowest_cost(c):
    minor_cost = float("inf")
    node_minor_cost = None
    for node_cost in c:
        current_cost = c[node_cost]
        if current_cost < minor_cost and node_cost not in processed:
            minor_cost = current_cost
            node_minor_cost = node_cost
    return node_minor_cost


node = find_lowest_cost(costs)
while node is not None:
    cost = costs[node]
    near = graph[node]
    for n in near.keys():
        new_cost = cost + near[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost(costs)
