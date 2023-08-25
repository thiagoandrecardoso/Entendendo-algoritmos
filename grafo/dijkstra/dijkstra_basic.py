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
    return "b"


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
