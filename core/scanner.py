# core/scanner.py
import subprocess

def scan_networks():
    try:
        result = subprocess.run(['iwlist', 'wlan0', 'scan'], capture_output=True, text=True)
        if result.returncode != 0:
            return []

        networks = []
        for line in result.stdout.split('\n'):
            if 'Cell' in line:
                network = {}
                network['ssid'] = ''
                network['bssid'] = ''
                network['signal'] = ''
                network['akm'] = ''
                networks.append(network)
            elif 'ESSID:' in line:
                networks[-1]['ssid'] = line.split('ESSID:')[1].strip().strip('"')
            elif 'Address:' in line:
                networks[-1]['bssid'] = line.split('Address:')[1].strip()
            elif 'Signal level=' in line:
                networks[-1]['signal'] = line.split('Signal level=')[1].split('/')[0].strip()
            elif 'IE: WPA Version 1' in line:
                networks[-1]['akm'] = 'WPA'
            elif 'IE: IEEE 802.11i/WPA2 Version 1' in line:
                networks[-1]['akm'] = 'WPA2'
        return networks
    except Exception as e:
        print(f"Error scanning networks: {e}")
        return []
