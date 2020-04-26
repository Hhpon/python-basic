import pywifi
from pywifi import const


def Check_state():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    print(ifaces.status())
    assert ifaces.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
    networkLists = ifaces.scan_results()
    for networkItem in networkLists:
        print(networkItem.ssid)
        print(networkItem.auth)
        print(networkItem.akm)
        print(networkItem.cipher)


Check_state()


