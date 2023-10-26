import os
def ping4(target):
    print("Pinging %s ..." % target)
    response = os.system("ping -c 1 " + target)
    return response

def ping6(target):
    print("Pinging %s ..." % target)
    response = os.system("ping6 -c 1 " + target)
    return response
