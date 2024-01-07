import subprocess
import json
import sys

def traceroute4(target):
    try:
        result = subprocess.check_output(['traceroute', target], universal_newlines=True)
        return result
    except subprocess.CalledProcessError:
        print(f"Error: Unable to traceroute {target}")
    
    return None

def traceroute6(target):
    try:
        result = subprocess.check_output(['traceroute6', target], universal_newlines=True)
        return result
    except subprocess.CalledProcessError:
        print(f"Error: Unable to traceroute {target}")
    
    return None

def traceroute_target(target, ipv4_en, ipv6_en):
    result_dict = {"traceroute": [
        {"IPv4": traceroute4(target)} if ipv4_en == 'ipv4' else {"IPv4": None},
        {"IPv6": traceroute6(target)} if ipv6_en == 'ipv6' else {"IPv6": None}
        ]}
    
    return json.dumps(result_dict)



if len(sys.argv) >= 3:
    print(traceroute_target(sys.argv[1], sys.argv[2], sys.argv[3]))
else:
    print("Error: Insufficient command line arguments.")
    print("Usage: python3 traceroute.py <target> <ipv4_en> <ipv6_en>")
