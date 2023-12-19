import requests
import json


class DnsManagerBeget:

    def __init__(self, login, passwd):
        self.login = login
        self.passwd = passwd
        self.base_url = 'https://api.beget.com/api/'

    def get_domain_ids(self):
        url = f'{self.base_url}domain/getList?login={self.login}&passwd={self.passwd}&output_format=json'
        response = requests.get(url)
        return response.json().get('result', [])

    def get_subdomain_info(self, subdomain):
        url = f'{self.base_url}dns/getData?login={self.login}&passwd={self.passwd}&input_format=json&output_format=json&input_data={{"fqdn":"{subdomain}"}}'
        return requests.get(url).json()

    def add_subdomain(self, sub, domain_id):
        url = f'{self.base_url}domain/addSubdomainVirtual?login={self.login}&passwd={self.passwd}&input_format=json&output_format=json&input_data={{"subdomain": "{sub}","domain_id":{domain_id}}}'
        return requests.get(url).json()

    def change_records(self, domain, a_records_ip):
        data = {
            "fqdn": domain,
            "records": {
                "A": [{"priority": 10, "value": a_records_ip}],
                "MX": [{"priority": 10, "value": "mx1.beget.ru"}, {"priority": 20, "value": "mx2.beget.ru"}],
                "TXT": [{"priority": 10, "value": "v=spf1 redirect=beget.com"}]
            }
        }
        url = f'{self.base_url}dns/changeRecords?login={self.login}&passwd={self.passwd}&input_format=json&output_format=json&input_data={json.dumps(data)}'
        return requests.get(url).json()


# Example
dns_manager = DnsManagerBeget(login='your_login', passwd='your_password')
print(dns_manager.get_subdomain_info(subdomain='test10.ziyodulla.uz'))
