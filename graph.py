
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
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High service throughput,https://grafana-k8s-ci.myntra.com/d/zuhbR77Vk/service-traffic-flow-and-health?orgId=1")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High Client throughput")
debug_graph.add_edge("High service throughput","Check rate limits")
debug_graph.add_edge("High Client throughput","Check with client")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High Ingress Latency,https://confluence.myntracorp.com/confluence/display/P13N/Service+Flow+Metrics#ingress_latency$https://confluence.myntracorp.com/confluence/display/P13N/Service+Flow+Metrics#https://confluence.myntracorp.com/confluence/display/P13N/Service+Flow+Metrics#linkerd_latency")
debug_graph.add_edge("High Ingress Latency", "Anomaly in CPU Usage for pod's node,https://grafana-k8s-ci.myntra.com/d/KTAjZ874z/kubernetes-node-to-pods-metrics?orgId=1&var-datasource=Thanos-querier&var-cluster=pac-sfcluster01&var-node=aks-worker3-37305883-vmss000002")
debug_graph.add_edge("High Ingress Latency", "Anomaly in Memory Usage for pod's node,https://grafana-k8s-ci.myntra.com/d/KTAjZ874z/kubernetes-node-to-pods-metrics?orgId=1&var-datasource=Thanos-querier&var-cluster=pac-sfcluster01&var-node=aks-worker3-37305883-vmss000002")
debug_graph.add_edge("Anomaly in Memory Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Anomaly in CPU Usage for pod's node", "Check with SRE team")
debug_graph.add_edge("Increased Latency at the Service Layer Across All/Specific APIs", "High Service Latency")
debug_graph.add_edge("High Service Latency", "High DBA Latency,https://confluence.myntracorp.com/confluence/display/P13N/Structured+debugging+2.0#Structureddebugging2.0-other_important_graphs$https://grafana-k8s-ci.myntra.com/d/CRJEXIUVk/redis-monitoring-prometheus?orgId=1&from=now-5m&to=now&var-odin_group=flockrediscache&var-hostname=pac-flockrediscache0&var-redis_port=6379$https://grafana-k8s-ci.myntra.com/d/zGcUKcDZz/namespace-view-aerospike-monitoring-stack?orgId=1&refresh=5m&var-Jobname=vectoraerospikenew-ci-vectoraerospikenew&var-cluster_name=vectoraerospikenew&var-node=All&var-namespace=All&var-DS_AEROSPIKE_PROMETHEUS=Thanos-querier$https://ecg-ci.myntra.com/d/_GV62ALVk/vorta-cassandra-ci?orgId=3&var-datacenter=newideaCIDC&var-cluster=New_IDEA_Cluster&var-keyspace=ideatokens&var-table=All&var-percentiles=99thpercentile&from=1701803311920&to=1701842890363$https://pmm-dbops.myntra.com/graph/d/mongodb-instance-summary/mongodb-instance-summary?from=now-5m&to=now&var-interval=1s&var-environment=All&var-cluster=FlockMongo&var-node_name=pac-flockmongodbe2&var-service_name=pac-flockmongodbe2&var-replication_set=All&var-database=All&var-node_type=All&var-service_type=All&var-username=All&var-schema=All&orgId=1&var-crop_host=All")
debug_graph.add_edge("High DBA Latency", "Check with DBA team")
debug_graph.add_edge("High Service Latency", "Check GC Metrics")

debug_graph.add_edge("Service API Throwing 5xx", "503")
debug_graph.add_edge("Service API Throwing 5xx", "502")
debug_graph.add_edge("Service API Throwing 5xx", "High CPU,https://grafana-k8s-ci.myntra.com/d/zuhbR77Vk/service-traffic-flow-and-health")
debug_graph.add_edge("Service API Throwing 5xx", "High Memory,https://grafana-k8s-ci.myntra.com/d/zuhbR77Vk/service-traffic-flow-and-health")
debug_graph.add_edge("Service API Throwing 5xx", "High Disk Usage,https://grafana-k8s-ci.myntra.com/d/zuhbR77Vk/service-traffic-flow-and-health")
debug_graph.add_edge("Service API Throwing 5xx", "Check receent code changes")
debug_graph.add_edge("Service API Throwing 5xx", "Check server logs")
debug_graph.add_edge("503", "Temporary server load")
debug_graph.add_edge("502", "Issue with external service")


