# 🛡️ Erick Phone Scanner - Hacker do Bem Luanda
# Uso ético: validar seus próprios números ou com consentimento
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

print("""
 ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
 ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
 ██████╔╝███████║██║   ██║██╔██╗ ██║███████╗
 ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║╚════██║
 ██║     ██║  ██║╚██████╔╝██║ ╚████║███████║
 ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
      Scanner Ético - Luanda AO - LVL 5
""")

# Prefixos Angola - Hacker do Bem sabe!
OPERADORAS_AO = {
    "92": "UNITEL Angola", "93": "UNITEL Angola",
    "91": "MOVICEL Angola", "99": "MOVICEL Angola",
    "94": "AFRICELL Angola", "95": "AFRICELL Angola"
}

def scan_numero(numero):
    try:
        # Se não tiver +244, assume Angola
        if not numero.startswith("+"):
            if numero.startswith("9"):
                numero = "+244" + numero
            else:
                numero = "+" + numero
        
        parsed = phonenumbers.parse(numero, None)
        
        print(f"\n[+] Analisando: {numero}")
        print("-"*40)
        print(f"✅ Válido: {phonenumbers.is_valid_number(parsed)}")
        print(f"📍 País: {geocoder.description_for_number(parsed, 'pt')}")
        print(f"📱 Tipo: {'Móvel' if phonenumbers.number_type(parsed) == 1 else phonenumbers.number_type(parsed)}")
        print(f"🌐 Operadora: {carrier.name_for_number(parsed, 'pt') or 'Desconhecida'}")
        print(f"🕐 Fuso: {timezone.time_zones_for_number(parsed)}")
        print(f"📞 Formato E164: {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}")
        
        # Check Angola manual
        num_str = str(parsed.national_number)
        prefix = num_str[:2]
        if prefix in OPERADORAS_AO:
            print(f"🇦🇴 Operadora AO confirmada: {OPERADORAS_AO[prefix]}")
        
        # Alerta ético
        if not phonenumbers.is_valid_number(parsed):
            print("\n⚠️ Número inválido ou não existe")
            
    except Exception as e:
        print(f"❌ Erro: {e} - Verifica o formato ex: +244924123456 ou 924123456")

while True:
    num = input("\nDigite o número (+2449XX ou 9XX) ou 'sair': ").strip()
    if num.lower() == 'sair':
        print("Saindo... Hacker do Bem desligando 🛡️")
        break
    if num:
        scan_numero(num)
