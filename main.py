import requests
import time
from data_structures.datacenter import Datacenter

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"

def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    status = False
    retry = 1
    while retry <= max_retries and status == False:
        try:
            r = requests.get(url)
            status = r.ok
            return r.json()
        except:
            print(f"Attempt {retry} of {max_retries} was not successfull.")
            time.sleep(delay_between_retries)
            retry += 1
            return {}
def main():
    """
    Main entry to our program.
    """
    data = get_data(URL)

    if not data:
        print ('No data')
        quit()

    datacenters = ( Datacenter(key, value)
                    for key, value in data.items() )

    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()
        nice_print(datacenter)

def nice_print(datacenter):
    print('Datacenter:', datacenter.name)
    for cluster in datacenter.clusters:
        print('\tCluster Name: ', cluster.name)
        print(2*'\t' + 'Security Level: ', cluster.security_level)
        for network in cluster.networks:
            print(2*'\t' + 'Network:', network.ipv4_network)
            print(3*'\t' + 'IP Addressess:')
            for ip_addresses in network.entries:
                print(4*"\t", '{}, available: {}, last user: {}'.format(ip_addresses.address, ip_addresses.available, ip_addresses.last_used))

if __name__ == '__main__':
    main()
