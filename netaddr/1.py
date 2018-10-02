import netaddr
def get_network(cidrstr):
    net=netaddr.IPNetwork(cidrstr)
    network= '%s/%s'%(net.network,net.prefixlen)
    return network

def test():
    ip = netaddr.IPAddress('192.168.20.32')
    print type(ip)

def compare(ip1,ip2):
    ip1=netaddr.IPAddress(ip1)
    ip2=netaddr.IPAddress(ip2)
    return ip1.value-ip2.value

def range():
    ip1 = '192.168.2.0'
    ip2 = '192.168.2.255'
    r1  = netaddr.IPRange(ip1, ip2)
    r2 = netaddr.IPNetwork('192.168.2.0/24')
    if r1 == r2:
        print 'yes'
    else:
        print 'No'

def ip_in_the_pool():
    ip1 = '192.168.2.0'
    ip2 = '192.168.2.255'
    ip_range = netaddr.IPRange(ip1, ip2)
    ip01 = '192.168.2.20'
    ip02 = '192.168.3.20'
    if ip01 in ip_range:
        print 'ip01 in iprange'
    else:
        print 'ip01 not in range'
    
    if ip02 in ip_range:
        print 'ip02 in iprange'
    else:
        print 'ip02 not in iprange'

def in_the_pool():
    ip0 = netaddr.IPAddress('192.168.2.22')
    ip1 = '192.168.2.21'
    ip2 = '192.168.2.200'
    ip_range = netaddr.IPRange(ip1, ip2)
    for ip in ip_range:
        if ip == ip0:
            print 'yes'
            break

def test1():
    cidr = '192.168.2.0/24'
    net = netaddr.IPNetwork(cidr)
    ip1 = netaddr.IPAddress('192.168.2.255')
    print net.network
    if net.netmask&ip1 == net.network:
        print 'yes'
    else:
        print 'no'

def test2():
    ip = '192.168.2.'
    ip_address = netaddr.IPAddress(ip)

test2()
