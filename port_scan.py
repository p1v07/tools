#py3
import ipaddress
import socket
import sys
from multiprocessing import Pool

def parse_hosts(cidr):
    if '/' in cidr:
        return [str(ip) for ip in ipaddress.IPv4Network(cidr)]
    else:
        return cidr

def port_scan(ip):
    port=3443
    try:
        tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if not tcp.connect_ex((ip,port)):
            print('[+] %s:%d/TCP open'%(ip,port))
            tcp.close()
    except Exception:
        pass

def main():

    hosts = parse_hosts(sys.argv[1])
    pool = Pool(10)
    pool.map(port_scan,hosts)
    pool.close()
    pool.join()

main()
