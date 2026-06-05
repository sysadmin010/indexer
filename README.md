<h1 align="center">
  <br>
  <a href="https://index3r.xyz/"><img src="https://i.imgur.com/a0JN7Rd.png" alt="INDEXER CLI" width="100%" style="border-radius: 8px; border: 1px solid #dc2626;"></a>
  <br>
  INDEXER CLI v1.1
  <br>
</h1>

<h4 align="center">El arsenal OSINT definitivo en tu terminal. Búsquedas masivas de inteligencia de amenazas, registros gubernamentales LATAM y Stealer Logs en milisegundos.</h4>

<p align="center">
  <a href="https://index3r.xyz/"><b>[ 🌐 WEB OFICIAL: INDEX3R.XYZ ]</b></a> •
  <a href="https://t.me/sysadmin010"><b>[ 💬 COMPRAR SUSCRIPCIÓN EN TELEGRAM ]</b></a>
</p>
### 🔍 Inteligencia de Cibercrimen (Data Breaches)
* **[1] EMAIL:** Ingresa un correo electrónico (ej: `admin@empresa.com`). El sistema barrerá terabytes de filtraciones globales (Combolists, Stealers, Dumps) y te devolverá las contraseñas en texto plano asociadas a ese correo.
* **[2] NICK:** Ingresa un nombre de usuario o alias (ej: `admin`). Rastrea la presencia de ese usuario a lo largo de foros hackeados, bases de datos y registros de juegos, vinculándolo con posibles correos y contraseñas.
* **[3] CONTRASEÑAS:** Ingresa una contraseña (ej: `admin1234`). La API realiza una búsqueda inversa para mostrarte qué correos o usuarios específicos utilizan o utilizaron esa contraseña exacta.
* **[9] URL-LOGS:** Ingresa un dominio corporativo (ej: `netflix.com`). Extrae todas las credenciales corporativas y cuentas de usuarios que han sido comprometidas y pertenecen a esa empresa.

### 🏛️ Inteligencia Gubernamental y Civil (LATAM)
* **[4] ARGENTINA:** Ingresa un DNI o CUIL. Extrae el dossier completo del objetivo incluyendo Nombres completos, Direcciones, Teléfonos celulares asociados, Fecha de Nacimiento e información fiscal (AFIP).
* **[5] PATENTE:** (Exclusivo Argentina). Ingresa el dominio/patente de un vehículo. Retorna datos del titular, radicación, chasis, motor y modelo exacto.
* **[6] PERÚ:** Ingresa un DNI peruano. Conecta con registros de RENIEC / EsSalud para devolver la ficha ciudadana completa.
* **[7] URUGUAY:** Módulo flexible. Permite ingresar un DNI, un Teléfono (con o sin el +598) o directamente Nombres y Apellidos. Busca a través de múltiples bases de datos consolidadas de Uruguay.

### 🕷️ Infraestructura y Malware
* **[8] MACHINES-LOGS (STL):** El módulo estrella. Busca en terabytes de registros de Redline, Vidar, Raccoon, etc. Ingresa un dominio o correo objetivo. La API te devolverá las rutas (`folder_path`) de los equipos infectados. *(Nota: La descarga del archivo .zip se realiza mediante el endpoint web documentado en nuestra API).*
* **[10] IP:** Ingresa una dirección IP (IPv4). Ejecuta un perfilado de red retornando Geolocalización exacta, ASN, Organización e ISP.
* **[11] WHOIS:** Ingresa un dominio. Retorna información de los servidores de nombres, registrador, fechas de creación/expiración y país de origen.

### ⚙️ Utilidades de la CLI
* **[H] AYUDA / HELP:** Despliega este mismo manual de forma resumida directamente en la terminal sin necesidad de salir del programa.
* **[L] IDIOMA / LANG:** Cambia toda la interfaz, banners y descripciones entre Español e Inglés al instante.
---

## 🛒 ¿CÓMO OBTENER ACCESO? (API KEY REQUIRED)
Este script es un cliente de alto rendimiento que conecta directamente con los clústeres privados de la suite **INDEXER**. Para que la herramienta funcione, **necesitas una API Key (Suscripción)**.

🔥 **¿Qué obtienes con tu suscripción a Indexer?**
* Acceso a más de **+66.000.000.000.000 (Trillones)** de credenciales expuestas.
* Bases de datos civiles y vehiculares exclusivas (Argentina, Perú, Uruguay).
* Motor de búsqueda de **Stealer Logs (Machines-Logs)** para descargar máquinas infectadas enteras (.zip).
* Consultas ilimitadas (sujetas a política de uso justo) y soporte directo.

👉 **Consigue tu acceso ahora en [https://index3r.xyz/](https://index3r.xyz/)** o contacta directamente al administrador oficial en Telegram: **[@sysadmin010](https://t.me/sysadmin010)**.

---

## 🛠️ INSTALACIÓN Y CONFIGURACIÓN

### 1. Clonar el repositorio
```bash
git clone [https://github.com/sysadmin010/indexer.git](https://github.com/sysadmin010/indexer.git)
cd indexer
