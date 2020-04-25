import pywifi


def Check_state():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    networkLists = ifaces.scan_results()
    for networkItem in networkLists:
        print(networkItem.ssid)


Check_state()
