from netmiko import ConnectHandler
import csv

# WAN1 = {
#     'device_type': 'cisco_ios_telnet',
#     'ip':   '172.17.1.151',
#     'username': 'cisco',
#     'password': 'cisco',
#     'secret': 'cisco',     # optional, defaults to ''
#     'verbose': True,       # optional, defaults to False
# }
#
# WAN2 = {
#     'device_type': 'cisco_ios_telnet',
#     'ip':   '172.17.1.152',
#     'username': 'cisco',
#     'password': 'cisco',
#     'secret': 'cisco',     # optional, defaults to ''
#     'verbose': True,       # optional, defaults to False
# }
# router_list = [WAN1,WAN2]


config_commands = ['crypto key generate rsa modulus 2048']

with open('devices.csv','rb') as csvfile:
    devices = csv.DictReader(csvfile)
    for router in devices:
        print("***Executing script on device:")
        print(router)
        print("***Script Output:")
        net_connect = ConnectHandler(**router)
        net_connect.enable()
        output = net_connect.send_config_set(config_commands)
        print(output)
        print("***device end***")
        net_connect.exit_enable_mode()


