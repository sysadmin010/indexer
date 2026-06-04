import requests
import json
import sys
import os
import datetime

API_URL = "https://index3r.xyz/api/execute"
DL_URL = "https://index3r.xyz/api/stl/download"

R = '\033[91m'  
G = '\033[92m'  
Y = '\033[93m'  
C = '\033[96m'  
W = '\033[97m'  
D = '\033[90m'  
X = '\033[0m'   

CURRENT_LANG = 'es'

LOCALE = {
    'es': {
        'sub': "Comprar suscripcion en https://index3r.xyz",
        'm_psw': "CONTRASEÑAS",
        'm_pat': "PATENTE",
        'm_mac': "MACHINES-LOGS",
        'm_url': "URL-LOGS",
        'm_hlp': "AYUDA / HELP",
        'm_lng': "IDIOMA / LANG",
        'h_title': "MANUAL DE USUARIO - MÓDULOS INDEXER",
        'h_uso': "Uso:",
        'h_ej': "Ejemplo de Target:",
        'h_desc': [
            ("1. EMAIL", "Busca credenciales (contraseñas, URLs) vinculadas a un correo en filtraciones (Breaches).", "usuario@gmail.com"),
            ("2. NICK", "Rastrea un nombre de usuario en bases de datos para encontrar correos y contraseñas asociadas.", "usuario123"),
            ("3. CONTRASEÑAS", "Busca qué correos o usuarios han utilizado una contraseña específica en filtraciones.", "P@ssw0rd123"),
            ("4. ARGENTINA", "Extrae datos civiles, comerciales y de contacto (DNI, Nombre, Teléfono, Dirección) en Argentina.", "12345678 (DNI sin puntos)"),
            ("5. PATENTE", "Consulta información vehicular (titular, modelo, año) de chapas patentes argentinas.", "ABC123 o AD123AA"),
            ("6. PERU", "Consulta información ciudadana en registros de Perú mediante número de DNI.", "12345678"),
            ("7. URUGUAY", "Consulta registros y datos de contacto de ciudadanos uruguayos.", "Apellido o DNI"),
            ("8. MACHINES-LOGS", "Busca en Stealer Logs (Malware). Devuelve rutas de carpetas infectadas con opción a descargar el .zip.", "netflix.com o usuario"),
            ("9. URL-LOGS", "Rastrea correos corporativos y registros vinculados a un dominio específico empresarial.", "empresa.com"),
            ("10. IP", "Geolocalización, proveedor de internet (ISP) y escaneo de información sobre una dirección IP.", "8.8.8.8"),
            ("11. WHOIS", "Obtiene datos de registro, información del dueño y servidores DNS de un dominio web.", "google.com")
        ],
        'no_records': "No se encontraron registros en la base de datos.",
        'gen_html': "--- GENERADOR DE REPORTE HTML ---",
        'html_prompt': "Nombre del archivo (ej. reporte_target.html): ",
        'html_success': "Reporte HTML generado exitosamente:",
        'html_err': "Error al guardar el archivo HTML:",
        'dl_title': "--- EXTRACCIÓN DE STEALER LOG ---",
        'dl_prompt1': "FOLDER_PATH a descargar (o Enter para omitir): ",
        'dl_prompt2': "Nombre del archivo .zip (ej. netflix_log.zip): ",
        'dl_conn': "Conectando con nodo de almacenamiento...",
        'dl_success': "Extracción completada. Archivo guardado como:",
        'dl_err_srv': "Error en el servidor: HTTP",
        'dl_err_net': "Error crítico de red:",
        'close_term': "Cerrando terminal...",
        'invalid_cmd': "Comando inválido.",
        'press_enter': "Presiona Enter para continuar...",
        'page_prompt': "Página (1 por defecto) ❯ ",
        'exec_mod': "Ejecutando módulo",
        'ask_html': "¿Deseas generar un reporte HTML de esta extracción? (S/n): ",
        'err_api': "API ERROR:",
        'err_crit': "ERROR CRÍTICO: No se pudo conectar a la API.",
        'err_user': "Ejecución interrumpida por el usuario.",
        'back_menu': "Presiona Enter para volver al menú principal...",
        'auth_req': "SI NO TIENES CLAVE COMPRA EN https://index3r.xyz",
        'auth_prompt': "Ingresa tu API Key ❯ ",
        'val_conn': "Validando API Key con el servidor central...",
        'val_ok': "Autenticación exitosa. Credenciales almacenadas localmente.",
        'val_fail': "Clave API rechazada o sin conexión.",
        'val_retry': "Presiona Enter para intentar de nuevo..."
    },
    'en': {
        'sub': "Purchase a subscription at https://index3r.xyz",
        'm_psw': "PASSWORDS",
        'm_pat': "LICENSE PLATE",
        'm_mac': "MACHINES-LOGS",
        'm_url': "URL-LOGS",
        'm_hlp': "HELP / AYUDA",
        'm_lng': "LANG / IDIOMA",
        'h_title': "USER MANUAL - INDEXER MODULES",
        'h_uso': "Usage:",
        'h_ej': "Target Example:",
        'h_desc': [
            ("1. EMAIL", "Searches for credentials (passwords, URLs) linked to an email in data breaches.", "user@gmail.com"),
            ("2. NICK", "Tracks a username across databases to find associated emails and passwords.", "user123"),
            ("3. PASSWORDS", "Searches which emails or users have used a specific password in breaches.", "P@ssw0rd123"),
            ("4. ARGENTINA", "Extracts civil, commercial, and contact data (ID, Name, Phone, Address) in Argentina.", "12345678 (ID without dots)"),
            ("5. LICENSE PLATE", "Queries vehicle information (owner, model, year) of Argentine license plates.", "ABC123 or AD123AA"),
            ("6. PERU", "Queries citizen information in Peruvian registries using ID number.", "12345678"),
            ("7. URUGUAY", "Queries registries and contact data of Uruguayan citizens.", "Lastname or ID"),
            ("8. MACHINES-LOGS", "Searches in Stealer Logs (Malware). Returns paths of infected folders with an option to download the .zip.", "netflix.com or user"),
            ("9. URL-LOGS", "Tracks corporate emails and records linked to a specific enterprise domain.", "company.com"),
            ("10. IP", "Geolocation, Internet Service Provider (ISP), and scanning of information about an IP address.", "8.8.8.8"),
            ("11. WHOIS", "Obtains registration data, owner info, and DNS servers of a web domain.", "google.com")
        ],
        'no_records': "No records found in the database.",
        'gen_html': "--- HTML REPORT GENERATOR ---",
        'html_prompt': "File name (e.g., report_target.html): ",
        'html_success': "HTML report successfully generated:",
        'html_err': "Error saving HTML file:",
        'dl_title': "--- STEALER LOG EXTRACTION ---",
        'dl_prompt1': "FOLDER_PATH to download (or Enter to skip): ",
        'dl_prompt2': "Name of the .zip file (e.g., netflix_log.zip): ",
        'dl_conn': "Connecting to storage node...",
        'dl_success': "Extraction completed. File saved as:",
        'dl_err_srv': "Server error: HTTP",
        'dl_err_net': "Critical network error:",
        'close_term': "Closing terminal...",
        'invalid_cmd': "Invalid command.",
        'press_enter': "Press Enter to continue...",
        'page_prompt': "Page (1 by default) ❯ ",
        'exec_mod': "Executing module",
        'ask_html': "Do you want to generate an HTML report of this extraction? (Y/n): ",
        'err_api': "API ERROR:",
        'err_crit': "CRITICAL ERROR: Could not connect to API.",
        'err_user': "Execution interrupted by user.",
        'back_menu': "Press Enter to return to the main menu...",
        'auth_req': "IF YOU DON'T HAVE A PASSWORD, BUY ON https://index3r.xyz",
        'auth_prompt': "Enter your API Key ❯ ",
        'val_conn': "Validating API Key with central server...",
        'val_ok': "Authentication successful. Credentials stored locally.",
        'val_fail': "API Key rejected or no connection.",
        'val_retry': "Press Enter to try again..."
    }
}

def t(key):
    return LOCALE[CURRENT_LANG][key]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_password(pwd):
    print(f"\n{C}[*] {t('val_conn')}{X}")
    payload = {
        "command": "ip",
        "target": "8.8.8.8",
        "password": pwd
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=15)
        data = response.json()
        
        # Si devuelve success, la key es válida
        if data.get("status") == "success":
            return True
        # Si la API tira un error, validamos que no sea un error de autenticación
        elif "error" in data:
            error_msg = str(data.get("error")).lower()
            if "password" in error_msg or "cred" in error_msg or "auth" in error_msg or "inv" in error_msg:
                return False
            return True
        return False
    except:
        return False

def get_api_password():
    key_file = "key.json"
    if os.path.exists(key_file):
        try:
            with open(key_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                pwd = data.get("password", "")
                if pwd:
                    return pwd
        except:
            pass

    # Bucle infinito hasta que se ingrese una key válida
    while True:
        clear_screen()
        print(f"{R}┌──[{W} {t('auth_req')} {R}]──────────────────────────{X}\n")
        pwd = input(f" {Y}{t('auth_prompt')}{W}").strip()
        
        if not pwd:
            continue
            
        if validate_password(pwd):
            print(f"{G}[+] {t('val_ok')}{X}")
            try:
                with open(key_file, 'w', encoding='utf-8') as f:
                    json.dump({"password": pwd}, f)
            except:
                pass
            return pwd
        else:
            print(f"{R}[-] {t('val_fail')}{X}")
            input(f"\n{D}{t('val_retry')}{X}")

PASSWORD = get_api_password()

def print_banner():
    banner = f"""{R}
    ██╗███╗   ██╗██████╗ ███████╗██╗  ██╗███████╗██████╗ 
    ██║████╗  ██║██╔══██╗██╔════╝╚██╗██╔╝██╔════╝██╔══██╗
    ██║██╔██╗ ██║██║  ██║█████╗   ╚███╔╝ █████╗  ██████╔╝
    ██║██║╚██╗██║██║  ██║██╔══╝   ██╔██╗ ██╔══╝  ██╔══██╗
    ██║██║ ╚████║██████╔╝███████╗██╔╝ ██╗███████╗██║  ██║
    ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{D}==============================================================
{R}INDEXER {W}{t('sub')} {R}v1.1
{D}=============================================================={X}
"""
    print(banner)

def print_menu():
    print(f"{R}[{W}1{R}]{D} EMAIL          {R}[{W}5{R}]{D} {t('m_pat').ljust(14)} {R}[{W}9{R}]{D} {t('m_url')}")
    print(f"{R}[{W}2{R}]{D} NICK           {R}[{W}6{R}]{D} PERU           {R}[{W}10{R}]{D} IP")
    print(f"{R}[{W}3{R}]{D} {t('m_psw').ljust(14)} {R}[{W}7{R}]{D} URUGUAY        {R}[{W}11{R}]{D} WHOIS")
    print(f"{R}[{W}4{R}]{D} ARGENTINA      {R}[{W}8{R}]{D} {t('m_mac').ljust(14)} {R}[{W}H{R}]{D} {t('m_hlp')}")
    print(f"                                                {R}[{W}L{R}]{D} {t('m_lng')}{X}\n")

def print_help():
    clear_screen()
    print_banner()
    print(f"{R}┌──[{W} {t('h_title')} {R}]──────────────────────────{X}\n")
    
    for cmd, desc, ex in t('h_desc'):
        print(f" {R}● {C}{cmd}{X}")
        print(f"   {D}{t('h_uso')} {W}{desc}{X}")
        print(f"   {D}{t('h_ej')} {G}{ex}{X}\n")
        
    print(f"{R}└───────────────────────────────────────────────────────────────────{X}")

def parse_results_cli(results):
    if not results:
        print(f"{Y}[!] {t('no_records')}{X}")
        return

    for idx, record in enumerate(results):
        print(f"\n{R}┌──[{W} RECORD #{idx + 1} {R}]{X}")
        
        if "formatted" in record and isinstance(record["formatted"], list):
            for line in record["formatted"]:
                if ":" in line:
                    parts = line.split(":", 1)
                    print(f"{R}│ {D}{parts[0].strip()}:{G} {parts[1].strip()}{X}")
                else:
                    print(f"{R}│ {G}{line}{X}")

        elif "datos_completos" in record:
            parts = record["datos_completos"].split("|")
            for part in parts:
                if ":" in part:
                    subparts = part.split(":", 1)
                    print(f"{R}│ {D}{subparts[0].strip()}:{G} {subparts[1].strip()}{X}")
                else:
                    print(f"{R}│ {G}{part.strip()}{X}")

        elif "datos" in record:
            datos_arr = record["datos"] if isinstance(record["datos"], list) else [record["datos"]]
            for line in datos_arr:
                formatted_line = line.replace(",", f" {R}|{G} ")
                print(f"{R}│ {D}DATA:{G} {formatted_line}{X}")

        elif "fields" in record:
            fields = record["fields"]
            if isinstance(fields, list):
                joined = f" {R}|{G} ".join(fields)
                joined = joined.replace(f"https {R}|{G} //", "https://").replace(f"http {R}|{G} //", "http://")
                print(f"{R}│ {R}BREACH_PAYLOAD:{G} {joined}{X}")
            else:
                print(f"{R}│ {R}BREACH_PAYLOAD:{G} {fields}{X}")

        else:
            for key, val in record.items():
                if key == "raw": continue
                val_str = json.dumps(val) if isinstance(val, (dict, list)) else str(val)
                
                if key.upper() == "FOLDER_PATH":
                    print(f"{R}│ {C}FOLDER_PATH:{W} {val_str}{X}")
                elif key.upper() == "URL":
                    print(f"{R}│ {D}URL:{C} {val_str}{X}")
                else:
                    print(f"{R}│ {D}{key.upper()}:{G} {val_str}{X}")
                    
        print(f"{R}└───────────────────────────────────────────────────{X}")


def generate_html_block(key, value):
    if value in ["\\N", "NULL", "", None] or key == "raw":
        return ""
    
    key_str = str(key).upper()
    val_str = str(value)
    item_style = ""
    key_style = ""

    if key_str == "BREACH_PAYLOAD":
        item_style = "grid-column: 1 / -1; background-color: rgba(220, 38, 38, 0.05); border-color: rgba(220, 38, 38, 0.3);"
        key_style = "color: #ef4444;"
        val_str = val_str.replace("https | //", "https://").replace("http | //", "http://")
    
    if key_str == "URL" and val_str.startswith("http"):
        val_str = f'<a href="{val_str}" target="_blank" style="color: #60a5fa; text-decoration: none;">{val_str}</a>'
        
    return f"""
    <div class="data-item" style="{item_style}">
        <span class="data-key" style="{key_style}">{key_str}</span>
        <span class="data-value">{val_str}</span>
    </div>
    """

def export_to_html(command, target, results):
    print(f"\n{D}{t('gen_html')}{X}")
    filename = input(f"{Y}[?] {t('html_prompt')}{W}").strip()
    if not filename:
        filename = f"reporte_{command}_{target}.html".replace("/", "_").replace(":", "")
    if not filename.endswith(".html"):
        filename += ".html"

    
    html_content = f"""<!DOCTYPE html>
<html lang="{CURRENT_LANG}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>INDEXER Report - {target}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        :root {{
            --bg-base: #050505; --bg-card: #111111;
            --border-subtle: #2a1111; --red-main: #dc2626;
            --text-primary: #f3f4f6; --text-secondary: #9ca3af; --text-data: #4ade80;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background-color: var(--bg-base); color: var(--text-primary);
            font-family: 'Inter', sans-serif; padding: 40px 20px;
            background-image: radial-gradient(circle at top, #0a0a0a 0%, #050505 100%);
        }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .header {{ border-bottom: 1px solid var(--border-subtle); padding-bottom: 20px; margin-bottom: 30px; }}
        .header h1 {{ color: var(--red-main); font-size: 1.8rem; letter-spacing: 2px; font-weight: 700; margin-bottom: 8px; }}
        .header p {{ color: var(--text-secondary); font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; }}
        .result-card {{
            background-color: var(--bg-card); border: 1px solid var(--border-subtle);
            border-top: 3px solid var(--red-main); border-radius: 8px; padding: 20px; margin-bottom: 20px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
        }}
        .result-header {{
            display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle);
            padding-bottom: 12px; margin-bottom: 16px; color: var(--text-secondary);
            font-size: 0.8rem; font-weight: 600; letter-spacing: 1px; text-transform: uppercase;
        }}
        .data-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }}
        .data-item {{ background-color: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 6px; padding: 12px; display: flex; flex-direction: column; gap: 4px; }}
        .data-key {{ color: var(--text-secondary); font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; }}
        .data-value {{ color: var(--text-data); font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; word-break: break-word; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>INDEXER INTELLIGENCE REPORT</h1>
            <p>TARGET: <span style="color: #fff;">{target}</span> | MODULE: <span style="color: #fff;">{command.upper()}</span> | DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
"""
    for idx, record in enumerate(results):
        html_content += f"""
        <div class="result-card">
            <div class="result-header"><span>RECORD_ID #{idx + 1}</span><span>MATCH FOUND</span></div>
            <div class="data-grid">
"""
        if "formatted" in record and isinstance(record["formatted"], list):
            for line in record["formatted"]:
                if ":" in line:
                    parts = line.split(":", 1)
                    html_content += generate_html_block(parts[0].strip(), parts[1].strip())
                else:
                    html_content += generate_html_block("INFO", line)
                    
        elif "datos_completos" in record:
            parts = record["datos_completos"].split("|")
            for part in parts:
                if ":" in part:
                    subparts = part.split(":", 1)
                    html_content += generate_html_block(subparts[0].strip(), subparts[1].strip())
                else:
                    html_content += generate_html_block("DATA", part.strip())
                    
        elif "datos" in record:
            datos_arr = record["datos"] if isinstance(record["datos"], list) else [record["datos"]]
            for line in datos_arr:
                html_content += generate_html_block("RAW PATENTE", line.replace(",", " | "))
                
        elif "fields" in record:
            fields = record["fields"]
            payload = " | ".join(fields) if isinstance(fields, list) else str(fields)
            html_content += generate_html_block("BREACH_PAYLOAD", payload)
            
        else:
            for key, val in record.items():
                html_content += generate_html_block(key, val)

        html_content += """
            </div>
        </div>"""

    html_content += """
    </div>
</body>
</html>"""

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"{G}[+] {t('html_success')} {W}{filename}{X}")
    except Exception as e:
        print(f"{R}[-] {t('html_err')} {e}{X}")


def download_stl():
    print(f"\n{D}{t('dl_title')}{X}")
    folder_path = input(f"{Y}[?] {t('dl_prompt1')}{W}").strip()
    
    if not folder_path:
        return

    output_name = input(f"{Y}[?] {t('dl_prompt2')}{W}").strip()
    if not output_name.endswith(".zip"):
        output_name += ".zip"

    print(f"\n{C}[*] {t('dl_conn')}{X}")
    
    params = {
        "folder_path": folder_path,
        "password": PASSWORD
    }

    try:
        req = requests.get(DL_URL, params=params, stream=True, timeout=60)
        if req.status_code == 200:
            with open(output_name, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"{G}[+] {t('dl_success')} {W}{output_name}{X}")
        else:
            print(f"{R}[-] {t('dl_err_srv')} {req.status_code}{X}")
    except Exception as e:
        print(f"{R}[-] {t('dl_err_net')} {e}{X}")


def main():
    global CURRENT_LANG

    commands_map = {
        "1": "email", "2": "nick", "3": "psw", "4": "arg",
        "5": "patente", "6": "peru", "7": "uruguay",
        "8": "stl", "9": "dl", "10": "ip", "11": "whois"
    }

    while True:
        clear_screen()
        print_banner()
        print_menu()
        
        cmd_choice = input(f"{R}INDEXER {D}❯ {W}").strip()
        
        if cmd_choice.lower() in ['exit', 'quit', '0']:
            print(f"{R}[!] {t('close_term')}{X}")
            break

        if cmd_choice.lower() in ['l', 'lang', 'idioma']:
            CURRENT_LANG = 'en' if CURRENT_LANG == 'es' else 'es'
            continue

        if cmd_choice.lower() in ['h', 'help']:
            print_help()
            input(f"\n{D}{t('press_enter')}{X}")
            continue

        if cmd_choice not in commands_map:
            print(f"{R}[-] {t('invalid_cmd')}{X}")
            input(f"\n{D}{t('press_enter')}{X}")
            continue

        command = commands_map[cmd_choice]
        target = input(f"{C}Target [{command}] {D}❯ {W}").strip()
        
        if not target:
            continue

        payload = {
            "command": command,
            "target": target,
            "password": PASSWORD
        }

        if command == "stl":
            page = input(f"{D}{t('page_prompt')}{W}").strip()
            payload["page"] = int(page) if page.isdigit() else 1

        print(f"\n{Y}[*] {t('exec_mod')} [{command.upper()}]...{X}")

        try:
            response = requests.post(API_URL, json=payload, timeout=30)
            data = response.json()

            if data.get("status") == "success":
                api_results = data.get("results") or data.get("data")
                
                if isinstance(api_results, list):
                    parse_results_cli(api_results)
                    
                    export_choice = input(f"\n{Y}[?] {t('ask_html')}{W}").strip().lower()
                    if export_choice in ['s', 'si', 'y', 'yes']:
                        export_to_html(command, target, api_results)

                elif isinstance(api_results, dict):
                    print(f"\n{R}┌──[{W} SINGLE NODE {R}]{X}")
                    for k, v in api_results.items():
                        print(f"{R}│ {D}{k.upper()}:{G} {v}{X}")
                    print(f"{R}└───────────────────────────────────────────────────{X}")
                else:
                    print(f"\n{G}{json.dumps(api_results, indent=2)}{X}")

                if command == "stl":
                    download_stl()

            else:
                print(f"{R}[-] {t('err_api')} {data.get('error', 'Error desconocido')}{X}")

        except requests.exceptions.RequestException as e:
            print(f"{R}[-] {t('err_crit')}{X}")

        input(f"\n{D}{t('back_menu')}{X}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] {t('err_user')}{X}")
        sys.exit(0)

