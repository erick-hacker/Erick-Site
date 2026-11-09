import requests, time
from datetime import datetime

print("=== ERICK BOT MONITOR LVL 4 ATIVADO ===")
print("Bot criado em Luanda - 09/11/2026")

alvo = input("Qual site vigiar? (ex: erick-hacker-do-bem.tiiny.site): ").strip()
if "http" not in alvo:
    alvo = "https://" + alvo

print(f"\n[INICIANDO VIGILANCIA] Alvo: {alvo}")
print("Pressione CTRL + C para parar\n")

tentativas = 0
while True:
    tentativas += 1
    hora = datetime.now().strftime("%H:%M:%S")
    try:
        r = requests.get(alvo, timeout=5)
        if r.status_code == 200:
            print(f"[{hora}] ✅ ONLINE - {alvo} - Status {r.status_code} - Check #{tentativas}")
        else:
            print(f"[{hora}] ⚠️ ALERTA - Status diferente: {r.status_code}")
    except Exception as e:
        print(f"[{hora}] 🚨 OFFLINE!!! {alvo} CAIU! Erro: {e}")
        # Aqui no futuro a gente coloca alerta no Telegram/WhatsApp
    
    # Espera 60 segundos antes de checar de novo
    time.sleep(60)
