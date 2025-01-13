import networkx as nx

def build_graph():
    G = nx.DiGraph()
    edges = [
        ("T1", "W1", 25), ("T1", "W2", 20), ("T1", "W3", 15),
        ("T2", "W3", 15), ("T2", "W4", 30), ("T2", "W2", 10),
        ("W1", "M1", 15), ("W1", "M2", 10), ("W1", "M3", 20),
        ("W2", "M4", 15), ("W2", "M5", 10), ("W2", "M6", 25),
        ("W3", "M7", 20), ("W3", "M8", 15), ("W3", "M9", 10),
        ("W4", "M10", 20), ("W4", "M11", 10), ("W4", "M12", 15),
        ("W4", "M13", 5), ("W4", "M14", 10)
    ]

    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    return G

# Algorithm implementation and max flow calculation
def calculate_max_flow(G, source, sink):
    flow_value, flow_dict = nx.maximum_flow(G, source, sink, flow_func=nx.algorithms.flow.edmonds_karp)
    return flow_value, flow_dict

# Map terminal and warehouse connections to stores
def map_terminal_to_store(flow_dict):
    result = []
    for terminal in ["T1", "T2"]:
        for warehouse, flow in flow_dict[terminal].items():
            if flow > 0:
                result.append((terminal, warehouse, flow))
            if warehouse in flow_dict:
                for store, sub_flow in flow_dict[warehouse].items():
                    if sub_flow > 0:
                        result.append((terminal, store, sub_flow))
    return result
