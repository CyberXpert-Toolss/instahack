import time
import random
import string
import sys
import os
from colorama import Fore, Style, init

# Inicializando o colorama
init(autoreset=True)

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir a arte ASCII INSTAHACK
def print_art():
    art = """
███ █   █  ████ █████  ███  █   █  ███   ███  █   █ 
 █  ██  █ █       █   █   █ █   █ █   █ █     █  █  
 █  █ █ █  ███    █   █████ █████ █████ █     ███   
 █  █  ██     █   █   █   █ █   █ █   █ █     █  █  
███ █   █ ████    █   █   █ █   █ █   █  ███  █   █ 
    """
    
    # Aplica efeito glitch nas cores
    lines = art.split('\n')
    for line in lines:
        if line.strip():
            # Efeito de cor aleatória entre vermelho e magenta
            color = random.choice([Fore.RED, Fore.MAGENTA, Fore.LIGHTRED_EX])
            print(color + line + Style.RESET_ALL)
            time.sleep(0.05)

# Função para efeito de digitação
def type_effect(text, delay=0.02, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Função para gerar IP aleatório
def random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"

# Função para gerar hash falso
def fake_hash():
    return ''.join(random.choices('0123456789abcdef', k=32))

# Função principal do ataque simulado ao Instagram
def instagram_attack(username):
    clear_screen()
    print_art()
    
    print(f"\n{Fore.RED}╔{'═'*58}╗")
    print(f"{Fore.RED}║{Fore.WHITE}  INSTAGRAM SECURITY ASSESSMENT TOOL v3.7{Fore.RED}              ║")
    print(f"{Fore.RED}║{Fore.WHITE}  Target: @{username}{Fore.RED}                                         ║")
    print(f"{Fore.RED}║{Fore.WHITE}  Started: {time.strftime('%H:%M:%S')}{Fore.RED}                                   ║")
    print(f"{Fore.RED}╚{'═'*58}╝{Style.RESET_ALL}")
    
    time.sleep(2)
    
    # Fase 1: Reconhecimento
    print(f"\n{Fore.RED}[{Fore.WHITE}*{Fore.RED}] {Fore.WHITE}PHASE 1: RECONNAISSANCE{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─'*50}{Style.RESET_ALL}")
    
    type_effect("[+] Scanning Instagram API endpoints...", 0.02, Fore.GREEN)
    time.sleep(1.2)
    
    endpoints = [
        "api.instagram.com/v1/users/search",
        "i.instagram.com/api/v1/users/web_profile_info",
        "graph.instagram.com/me",
        "api.instagram.com/v1/friendships/show"
    ]
    
    for endpoint in endpoints:
        sys.stdout.write(f"{Fore.CYAN}    └─ Testing: {endpoint}")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write(f" {Fore.GREEN}[200 OK]{Style.RESET_ALL}\n")
        sys.stdout.flush()
    
    print(f"\n{Fore.GREEN}[+] Target profile found: @{username}")
    print(f"{Fore.GREEN}[+] Account status: ACTIVE")
    print(f"{Fore.GREEN}[+] Privacy setting: PUBLIC")
    print(f"{Fore.GREEN}[+] 2FA Enabled: FALSE{Style.RESET_ALL}")
    
    time.sleep(1.5)
    
    # Fase 2: Enumeração
    print(f"\n{Fore.RED}[{Fore.WHITE}*{Fore.RED}] {Fore.WHITE}PHASE 2: ENUMERATION{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─'*50}{Style.RESET_ALL}")
    
    type_effect("[+] Gathering OSINT data...", 0.02, Fore.GREEN)
    time.sleep(1)
    
    emails = ['@gmail.com', '@hotmail.com', '@outlook.com', '@yahoo.com', '@proton.me']
    dados = [
        f"Email: {username}{random.choice(emails)}",
        f"Phone: +55 {random.randint(11,99)} 9{random.randint(1000,9999)}-{random.randint(1000,9999)}",
        f"Posts: {random.randint(0,3)}",
        f"Followers: 1",
        f"Following: 0",
        f"Created: {random.randint(2023,2024)}/{random.randint(1,12):02d}/{random.randint(1,28):02d}"
    ]
    
    for dado in dados:
        print(f"{Fore.CYAN}    └─ {dado}")
        time.sleep(0.3)
    
    time.sleep(1)
    
    # Fase 3: Ataque de Força Bruta
    print(f"\n{Fore.RED}[{Fore.WHITE}*{Fore.RED}] {Fore.WHITE}PHASE 3: PASSWORD CRACKING{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─'*50}{Style.RESET_ALL}")
    
    type_effect("[+] Initializing dictionary attack...", 0.02, Fore.GREEN)
    time.sleep(1)
    
    # Simula conexão com proxies
    print(f"\n{Fore.MAGENTA}[~] Connecting to proxy network...{Style.RESET_ALL}")
    for i in range(5):
        ip = random_ip()
        port = random.choice([8080, 3128, 8888, 1080, 443, 80])
        sys.stdout.write(f"{Fore.MAGENTA}    └─ Proxy {i+1}: {ip}:{port}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f" {Fore.GREEN}[CONNECTED]{Style.RESET_ALL}\n")
        sys.stdout.flush()
    
    print(f"\n{Fore.GREEN}[+] Dictionary loaded: rockyou_2024.txt")
    print(f"{Fore.GREEN}[+] Wordlist size: 14,341,564 passwords")
    print(f"{Fore.GREEN}[+] Rate: ~{random.randint(800,1200)} attempts/second{Style.RESET_ALL}")
    
    time.sleep(1)
    
    # Barra de progresso do ataque
    print(f"\n{Fore.CYAN}[~] Executing brute force attack...{Style.RESET_ALL}\n")
    
    for i in range(0, 101, 2):
        barra = '█' * (i // 2) + '░' * (50 - i // 2)
        password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 12)))
        sys.stdout.write(f"\r{Fore.CYAN}[{barra}] {i}% | Testing: {password:<15}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)
    
    # Senha "encontrada" - MAIS VISÍVEL
    possible_passwords = [
        "instagram123", "password123", "qwerty2024", "admin123",
        "iloveyou2024", "princess", "dragonball", "pokemon123"
    ]
    found_password = random.choice(possible_passwords)
    
    print(f"\n")
    print(f"{Fore.GREEN}╔{'═'*50}╗")
    print(f"{Fore.GREEN}║{Fore.WHITE}  [+] PASSWORD CRACKED SUCCESSFULLY!{Fore.GREEN}        ║")
    print(f"{Fore.GREEN}╠{'═'*50}╣")
    print(f"{Fore.GREEN}║{Fore.RED}  {found_password}{Fore.GREEN}                            ║")
    print(f"{Fore.GREEN}╚{'═'*50}╝{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}[!] Attempts: {random.randint(5432, 12678)}")
    print(f"{Fore.YELLOW}[!] Time elapsed: {random.uniform(3.2, 8.7):.2f} seconds{Style.RESET_ALL}")
    
    time.sleep(1.5)
    
    # Fase 4: Extração de Dados
    print(f"\n{Fore.RED}[{Fore.WHITE}*{Fore.RED}] {Fore.WHITE}PHASE 4: DATA EXTRACTION{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─'*50}{Style.RESET_ALL}")
    
    type_effect("[+] Establishing secure connection...", 0.02, Fore.GREEN)
    time.sleep(1)
    
    print(f"\n{Fore.CYAN}[~] Downloading account data:{Style.RESET_ALL}")
    
    data_types = [
        "Profile information", "Private messages", "Photos/Videos",
        "Stories archive", "Saved posts", "Search history",
        "Location data", "Contact list"
    ]
    
    for data in data_types:
        sys.stdout.write(f"{Fore.CYAN}    └─ {data:<25}")
        sys.stdout.flush()
        time.sleep(0.3)
        size = random.uniform(0.1, 15.4)
        sys.stdout.write(f" {Fore.GREEN}[{size:.1f} MB]{Style.RESET_ALL}\n")
        sys.stdout.flush()
    
    print(f"\n{Fore.GREEN}[+] Total data extracted: {random.uniform(25, 80):.1f} MB")
    print(f"{Fore.GREEN}[+] Data saved to: /root/insta_dumps/{username}/{Style.RESET_ALL}")
    
    time.sleep(1.5)
    
    # Fase 5: Cobertura de Rastros
    print(f"\n{Fore.RED}[{Fore.WHITE}*{Fore.RED}] {Fore.WHITE}PHASE 5: COVERING TRACKS{Style.RESET_ALL}")
    print(f"{Fore.RED}{'─'*50}{Style.RESET_ALL}")
    
    type_effect("[+] Clearing server logs...", 0.02, Fore.GREEN)
    time.sleep(0.8)
    type_effect("[+] Rotating proxy chain...", 0.02, Fore.GREEN)
    time.sleep(0.8)
    type_effect("[+] Deleting temporary files...", 0.02, Fore.GREEN)
    time.sleep(0.8)
    type_effect("[+] Spoofing MAC address...", 0.02, Fore.GREEN)
    time.sleep(0.8)
    
    # Mensagem final
    print(f"\n{Fore.RED}╔{'═'*58}╗")
    print(f"{Fore.RED}║{Fore.GREEN}  OPERATION COMPLETED SUCCESSFULLY{Fore.RED}                       ║")
    print(f"{Fore.RED}╠{'═'*58}╣")
    print(f"{Fore.RED}║{Fore.WHITE}  Target: @{username}{Fore.RED}                                          ║")
    print(f"{Fore.RED}║{Fore.WHITE}  Password: {Fore.RED}{found_password}{Fore.RED}                                    ║")
    print(f"{Fore.RED}║{Fore.WHITE}  Session: {fake_hash()}{Fore.RED}  ║")
    print(f"{Fore.RED}╚{'═'*58}╝{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}Press Enter to exit...{Style.RESET_ALL}")
    input()

# Execução principal
if __name__ == "__main__":
    try:
        clear_screen()
        print(f"{Fore.RED}[{Fore.WHITE}*{Fore.RED}] {Fore.WHITE}Loading Instagram Security Framework...{Style.RESET_ALL}")
        time.sleep(1.5)
        
        username = input(f"\n{Fore.RED}[{Fore.WHITE}?{Fore.RED}] {Fore.WHITE}Enter Instagram username: {Fore.RED}@")
        
        if not username:
            print(f"{Fore.RED}[!] No username provided. Exiting...{Style.RESET_ALL}")
            sys.exit()
        
        instagram_attack(username)
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}[!] Operation cancelled by user.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Cleaning up...{Style.RESET_ALL}")
        time.sleep(1)
        print(f"{Fore.GREEN}[+] Clean exit.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error: {e}{Style.RESET_ALL}")
