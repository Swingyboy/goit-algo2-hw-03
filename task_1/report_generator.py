from jinja2 import Template


def generate_html_report(flow_value, terminal_to_store):
    # Calculate total flow per terminal
    terminal_flow = {}
    for terminal, store, flow in terminal_to_store:
        if terminal not in terminal_flow:
            terminal_flow[terminal] = 0
        terminal_flow[terminal] += flow

    # Identify routes with the smallest flow
    min_flow_routes = [route for route in terminal_to_store if route[2] == min(terminal_to_store, key=lambda x: x[2])[2]]

    # Identify stores receiving the least goods
    store_flow = {}
    for _, store, flow in terminal_to_store:
        if store not in store_flow:
            store_flow[store] = 0
        store_flow[store] += flow
    min_flow_stores = [store for store, flow in store_flow.items() if flow == min(store_flow.values())]

    # Generate conclusions
    conclusions = f"""
    <h2>Conclusions</h2>
    <ol>
        <li><strong>Terminals with the highest flow of goods to stores:</strong><br>
            {', '.join([f"{terminal} ({flow} units)" for terminal, flow in sorted(terminal_flow.items(), key=lambda item: item[1], reverse=True)])}
        </li>
        <li><strong>Routes with the smallest capacity:</strong><br>
            {', '.join([f"{route[0]} to {route[1]} ({route[2]} units)" for route in min_flow_routes])}.<br>
            These routes limit the total flow to the respective stores.
        </li>
        <li><strong>Stores receiving the least goods:</strong><br>
            {', '.join([f"{store} ({store_flow[store]} units)" for store in min_flow_stores])}.<br>
            Increasing the capacity of routes leading to these stores could enhance their supply.
        </li>
        <li><strong>Bottlenecks in the logistics network:</strong><br>
            Routes with minimal capacity, such as those identified above, act as bottlenecks. Enhancing their capacity can improve the overall efficiency of the logistics network.
        </li>
    </ol>
    """

    # HTML template
    template = Template("""
    <html>
    <head>
        <title>Logistics Network Flow Report</title>
    </head>
    <body>
        <h1>Logistics Network Flow Report</h1>
        <p><strong>Max Flow:</strong> {{ flow_value }}</p>
        <h2>Terminal to Store Flows</h2>
        <table border="1">
            <thead>
                <tr>
                    <th>Terminal</th>
                    <th>Store</th>
                    <th>Flow (units)</th>
                </tr>
            </thead>
            <tbody>
                {% for terminal, store, flow in terminal_to_store %}
                <tr>
                    <td>{{ terminal }}</td>
                    <td>{{ store }}</td>
                    <td>{{ flow }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {{ conclusions | safe }}
    </body>
    </html>
    """)

    # Render and write the HTML report
    with open("logistics_report.html", "w") as f:
        f.write(template.render(flow_value=flow_value, terminal_to_store=terminal_to_store, conclusions=conclusions))
