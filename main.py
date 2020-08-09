import requests
import time
import math
import sys

def requester(url, timeout):
    i = 0

    while True:
        now = time.time()   
        time.sleep(timeout)

        # make request to the url
        request = requests.get(url)

        # parse the request header info...
        req = "%s - %s - %s sec" % (
            request.status_code, 
            request.headers['Content-Type'], 
            math.floor(time.time() - now)
            )
        
        if request.status_code == 404 and i == 4:
            sys.exit()

        i += 1
        print (req)


if __name__ == "__main__":
    requester(
        str(input("url: ")), 
        int(input("timeout: "))) 