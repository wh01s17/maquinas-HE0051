# Laboratorios de Pentesting Guiado

> ⚠️ **Todas las máquinas de este repositorio fueron obtenidas desde [HackMyVM](https://hackmyvm.eu/) y [Vulnyx](https://vulnyx.com/), ambas  son plataformas de laboratorios de hacking ético gratuitas.**  
> El propósito de este repositorio es exclusivamente educativo.

Este repositorio contiene una colección de laboratorios prácticos diseñados para simular escenarios reales de pruebas de penetración. Cada laboratorio sigue las fases establecidas por la metodología **PTES** (Penetration Testing Execution Standard) o la **OWASP Testing Guide v4**, permitiendo desarrollar habilidades técnicas en:

- Recolección de información  
- Análisis de servicios expuestos  
- Explotación de vulnerabilidades web y de red  
- Escalada de privilegios  
- Post-explotación  

---

## 🖥️ Tabla de Máquinas

| Nº  | Nombre de la Máquina       | Vulnerabilidades Principales                                                                     | Dificultad | Link a la máquina |
|-----|----------------------------|--------------------------------------------------------------------------------------------------|------------|-------------------|
| 00  | simple                     | SMB mal configurado, servicios web expuestos, escalada de privilegios en Windows                 | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Simple) |
| 01  | whitedoor                  | FTP anónimo, explotación web (credenciales), escalada de privilegios en Linux                    | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Whitedoor) |
| 02  | talk                       | SQL Injection, escalada de privilegios en Linux                                                  | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Talk) |
| 03  | preload                    | Server-Side Template Injection (SSTI) en Flask, RCE, escalada a root                             | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Preload) |
| 04  | system                     | XXE (XML External Entity), acceso vía SSH, Python Library Hijacking                              | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=System) |
| 05  | faust                      | CMS Made Simple 2.2.5 vulnerable, tarea automatizada mal configurada, RCE                        | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Faust) |
| 06  | twisted                    | Esteganografía, abuse de capabilities, ingeniería inversa, escalada local de privilegios         | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Twisted) |
| 07  | visions                    | Metadatos con información sensible, contraseñas débiles, configuración insegura de sudo          | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Visions) |
| 08  | driftingblues9             | Vulnerabilidades conocidas en web, análisis de binarios, buffer overflow (BOF)                   | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Driftingblues9) |
| 09  | tornado                    | SQL Truncation Attack, ejecución remota de comandos, abuso de permisos sudo                      | Medium     |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Tornado) |
| 10  | medusa                     | LFI, log poisoning, fuerza bruta SSH, volcado de memoria, análisis de archivos cifrados          | Easy       |[HMV](https://hackmyvm.eu/machines/machine.php?vm=Medusa) |
| 11  | hit                        | Explotación de repositorios expuestos, descubrimiento de puertos mediante port knocking, crackeo de claves SSH   | Easy       |[Vulnyx](https://vulnyx.com/#hit) |

---

## 📚 Metodologías Aplicadas

- **PTES** – [penetration-testing-standard.org](http://www.pentest-standard.org/)
- **OWASP Testing Guide v4** – [owasp.org](https://owasp.org/www-project-web-security-testing-guide/)

---

## 🛠️ Requisitos

- VirtualBox o VMware
- Kali Linux o cualquier distribución con herramientas de pentesting
- Python3, netcat, nmap, burpsuite, etc.

---

## 🚧 Estado

> En desarrollo. Se irán agregando writeups y scripts de cada laboratorio conforme se completen.

---

## 📄 Licencia

Este repositorio está disponible bajo la licencia MIT. Solo para fines educativos. No realizar pruebas en sistemas sin autorización explícita.
