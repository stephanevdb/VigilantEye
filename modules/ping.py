import subprocess
import json
import sys

def ping4(target):
    try:
        result = subprocess.check_output(['ping', '-c', '1', target], universal_newlines=True)
        time_index = result.find('time=')
        if time_index != -1:
            time_start = time_index + len('time=')
            time_end = result.find(' ', time_start)
            time_value = result[time_start:time_end]
            return f"{float(time_value)}ms"
    except subprocess.CalledProcessError:
        print(f"Error: Unable to ping {target}")
    
    return None

def ping6(target):
    try:
        result = subprocess.check_output(['ping6', '-c', '1', target], universal_newlines=True)
        time_index = result.find('time=')
        if time_index != -1:
            time_start = time_index + len('time=')
            time_end = result.find(' ', time_start)
            time_value = result[time_start:time_end]
            return f"{float(time_value)}ms"
    except subprocess.CalledProcessError:
        print(f"Error: Unable to ping {target}")
    
    return None

def ping_target(target, ipv4_en, ipv6_en):
    result_dict = {}
    
    if ipv4_en == 'ipv4':
        result_dict['IPv4'] = ping4(target)
    if ipv6_en == 'ipv6':
        result_dict['IPv6'] = ping6(target)
    
    return json.dumps(result_dict)

print("Running ping.py...")
print(sys.argv)
print("Target:", sys.argv[1])
print("IPv4:", sys.argv[2])
print("IPv6:", sys.argv[3])
if len(sys.argv) >= 3:
    print(ping_target(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
    print("Error: Insufficient command line arguments.")
    print("Usage: python3 ping.py <target> <ipv4_en> <ipv6_en>")
