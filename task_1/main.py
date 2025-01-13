from graph_utils import build_graph, calculate_max_flow, map_terminal_to_store
from report_generator import generate_html_report

# Main script
def main():
    G = build_graph()
    G.add_node('S')
    G.add_node('T')
    for terminal in ['T1', 'T2']:
        G.add_edge('S', terminal, capacity=float('inf'))
    for store in [f'M{i}' for i in range(1, 15)]:
        G.add_edge(store, 'T', capacity=float('inf'))

    flow_value, flow_dict = calculate_max_flow(G, 'S', 'T')

    print(f"Max Flow: {flow_value}")

    terminal_to_store = map_terminal_to_store(flow_dict)

    print("\nTerminal to Store Flows:")
    for terminal, store, flow in terminal_to_store:
        print(f"{terminal} -> {store}: {flow}")

    generate_html_report(flow_value, terminal_to_store)
    print("\nReport generated: logistics_report.html")


if __name__ == "__main__":
    main()
