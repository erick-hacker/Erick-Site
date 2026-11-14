import requests, time
from datetime import datetime

ALVO = "https://erick-hacker-do-bem.tiiny.site"
ARQUIVO_LOG = "erick_monitor_log.txt"

print("=== ERICK BOT FINAL LVL 4 - SEM TELEGRAM ===")
print(f"Vigiando: {ALVO}")
print("Log salvo em: erick_monitor_log.txt\n")

# Cria log inicial
with open(ARQUIVO_LOG, "a") as f:
    f.write(f"\n--- MONITOR INICIADO {datetime.now()} ---\n")

checks = 0
while True:
    checks += 1
    hora = datetime.now().strftime("%d/%m %H:%M:%S")
    try:
        r = requests.get(ALVO, timeout=5)
        if r.status_code == 200:
            print(f"[{hora}] ✅ ONLINE - Check #{checks}")
            # Salva só se cair pra não encher o log
        else:
            msg = f"[{hora}] ⚠️ Status {r.status_code} - {ALVO}"
            print(msg)
            with open(ARQUIVO_LOG, "a") as f:
                f.write(msg + "\n")
    except Exception as e:
        msg = f"[{hora}] 🚨 OFFLINE!!! {ALVO} - Erro: {e}"
        print(msg + " \a")  # \a faz beep no celular!
        with open(ARQUIVO_LOG, "a") as f:
            f.write(msg + "\n")
        # Toca som 3x
        print("🔔🔔🔔 SITE CAIU!!! 🔔🔔🔔")
    
    time.sleep(60)
