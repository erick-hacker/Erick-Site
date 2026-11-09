import socket, requests

def scan_portas(ip):
    print(f"\n[SCAN PORTAS] {ip}")
    for p in [21,22,80,443,8080]:
        s=socket.socket()
        s.settimeout(0.5)
        if s.connect_ex((ip,p))==0:
            print(f"  Porta {p} ABERTA!")
        s.close()

def rastreia_ip(ip):
    try:
        r=requests.get(f"http://ip-api.com/json/{ip}").json()
        print(f"\n[RASTREIO] {ip}")
        print(f"  Pais: {r['country']} - {r['city']}")
        print(f"  Provedor: {r['isp']}")
        print(f"  Coords: {r['lat']},{r['lon']}")
    except:
        print("  Erro no rastreio")

print("=== ERICK MASTER TOOL LVL 3 ===")
alvo = input("Digite um IP ou dominio: ").strip()

# Descobre IP se for dominio
try:
    ip_real = socket.gethostbyname(alvo)
    print(f"IP de {alvo} é {ip_real}")
    rastreia_ip(ip_real)
    scan_portas(ip_real)
except Exception as e:
    print(f"Erro: {e}")

print("\nFIM - Relatorio salvo? Copia e cola no teu portfolio!")
