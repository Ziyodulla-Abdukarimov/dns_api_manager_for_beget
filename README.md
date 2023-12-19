# BEGET DNS API INTEGRATION

### Requirements packages
```
pip install requests
```

### Usage example
```
dns_manager = DnsManagerBeget(login='your_login', passwd='your_password')
print(dns_manager.get_subdomain_info(subdomain='test10.domain.uz'))
```
