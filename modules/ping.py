import subprocess
import json

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