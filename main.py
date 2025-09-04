from utils.email import send_email, generate_mail_body
import os
import subprocess
# import dotenv

# dotenv.load_dotenv()

dominios = os.getenv("DOMINIOS").split(";")
receptores = os.getenv("RECEPTORES").split(";")

failed_domains = []

for dominio in dominios:
    try:
        result = subprocess.run(
            ["ping", "-c", "1", dominio],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
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