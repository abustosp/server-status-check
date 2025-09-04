from utils.email import send_email, generate_mail_body
import os
import subprocess
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv no está instalado, no se cargarán las variables de entorno, salvo que se usen en el .env.")

dominios = os.getenv("DOMINIOS").split(";")
receptores = os.getenv("RECEPTORES").split(";")
timeout = int(os.getenv("TIMEOUT", 60))

failed_domains = []

for dominio in dominios:
    try:
        result = subprocess.run(
            ["ping", "-c", "1", dominio],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout
        )
        if result.returncode != 0:
            failed_domains.append(dominio)
    except Exception:
        failed_domains.append(dominio)

if failed_domains:
    body = generate_mail_body(failed_domains)
    subject = f"FALLA EN SERVICIOS ({len(failed_domains)})"
    for receptor in receptores:
        send_email(
            to_email=receptor,
            subject=subject,
            body=body
        )
else:
    print("TODOS LOS DOMINIOS FUNCIONAN CORRECTAMENTE")