import socket
import subprocess
import threading
from datetime import datetime

print("""
 ███████╗██████╗ ██╗ ██████╗██╗  ██╗
 ██╔════╝██╔══██╗██║██╔════╝██║ ██╔╝
 █████╗  ██████╔╝██║██║     █████╔╝ 
 ██╔══╝  ██╔══██╗██║██║     ██╔═██╗ 
 ███████╗██║  ██║██║╚██████╗██║  ██╗
 ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝
       AI NETWORK SCANNER v1.0
       by ERICK - Só use na tua rede!
""")

# Pega teu IP local
def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        ip = '192.168.1.1'
    finally:
        s.close()
    return ip

my_ip = get_my_ip()
base_ip = '.'.join(my_ip.split('.')[:-1]) + '.'
print(f"[+] Teu IP: {my_ip}")
print(f"[+] Escaneando rede: {base_ip}0/24\n")

# Escanear
ativos = []

def ping_ip(ip):
    try:
        # funciona no Termux / Linux
        res = subprocess.run(['ping','-c','1','-W','1', ip], 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0:
            try:
                nome = socket.gethostbyaddr(ip)[0]
            except:
                nome = "Desconhecido"
            print(f"[ON] {ip} - {nome}")
            ativos.append((ip, nome))
    except:
        pass

threads = []
for i in range(1, 255):
    ip = f"{base_ip}{i}"
    t = threading.Thread(target=ping_ip, args=(ip,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(f"\n[✓] Scan finalizado! {len(ativos)} dispositivos encontrados:")
for ip, nome in ativos:
    print(f"  -> {ip} | {nome}")

# Scanner de portas rápido
alvo = input("\nDigita um IP pra escanear portas (ou enter pra sair): ")
if alvo:
    print(f"\n[*] Escaneando portas de {alvo}...")
    portas_comuns = [21,22,23,80,443,8080,3306,5432]
    for porta in portas_comuns:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((alvo, porta))
        if result == 0:
            print(f"[ABERTA] Porta {porta}")
        sock.close()
