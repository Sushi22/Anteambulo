class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

debug_graph = Graph()

debug_graph.add_edge("issues", "Increased Latency at the Service Layer Across All/Specific APIs")
debug_graph.add_edge("issues","Service API Throwing 5xx")

debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "Issue after deployment")
debug_graph.add_edge("Issue after deployment", "Revert Deployment")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High service throughput")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High Client throughput")
debug_graph.add_edge("High service throughput","Check rate limits")
debug_graph.add_edge("High Client throughput","Check with client")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High Ingress Latency")
debug_graph.add_edge("High Ingress Latency", "Anomaly in CPU Usage for pod's node")
debug_graph.add_edge("High Ingress Latency", "Anomaly in Memory Usage for pod's node")
debug_graph.add_edge("Anomaly in Memory Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High Service Latency")
debug_graph.add_edge("High Service Latency", "High DBA Latency")
debug_graph.add_edge("High DBA Latency", "Check with DBA team")
debug_graph.add_edge("High Service Latency", "Check GC Metrics")

debug_graph.add_edge("Service API Throwing 5xx", "503")
debug_graph.add_edge("Service API Throwing 5xx", "502")
debug_graph.add_edge("Service API Throwing 5xx", "High CPU")
debug_graph.add_edge("Service API Throwing 5xx", "High Memory")
debug_graph.add_edge("Service API Throwing 5xx", "High Disk Usage")
debug_graph.add_edge("Service API Throwing 5xx", "Check receent code changes")
debug_graph.add_edge("Service API Throwing 5xx", "Check server logs")
debug_graph.add_edge("503", "Temporary server load")
debug_graph.add_edge("502", "Issue with external service")







