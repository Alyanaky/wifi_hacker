# core/scanner.py

import pywifi

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    iface.scan()
    results = iface.scan_results()
    networks = []
    for network in results:
        networks.append({
            'ssid': network.ssid,
            'bssid': network.bssid,
            'signal': network.signal,
            'akm': network.akm
        })
    return networks
