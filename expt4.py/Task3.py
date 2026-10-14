server_ip = ("192.168.1.1", 8080)
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips(ip):
    allowed_ips.append(ip)

def display_config():
    print("Server IP:", server_ip)
    print("Allowed IPs:", allowed_ips)

update_allowed_ips("192.168.1.4")

display_config()