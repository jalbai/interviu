import re
from data_structures.cluster import Cluster

class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.
        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = [
            Cluster(
                name=key,
                security_level=value['security_level'],
                networks=value['networks']
            )
            for key, value in cluster_dict.items()
        ]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        valid_cluster_name = self.name[0:3].upper()

        find_format = r'^{}-\d{{1,3}}$'.format(valid_cluster_name)
        pattern = re.compile(find_format)

        clusters = self.clusters
        remove = []

        for cluster in clusters:
            if not pattern.match(cluster.name):
                remove.append(cluster.name)

        self.clusters = [x for x in clusters if x.name not in remove]
