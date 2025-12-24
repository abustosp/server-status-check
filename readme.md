# Server Status Check

Script en Python para monitorear dominios con `ping` y enviar alertas por correo cuando alguno no responde.

## Que hace
- Lee dominios desde `DOMINIOS`.
- Ejecuta `ping -c 1` por dominio con timeout configurable.
- Si hay fallos, envia un correo HTML a los receptores.

## Requisitos
- Python 3.9+
- Comando `ping` disponible en el sistema
- Opcional: `python-dotenv` para cargar `.env`
- Acceso a un servidor SMTP

## Configuracion (variables de entorno)
- `DOMINIOS`: dominios separados por `;`.
- `TIMEOUT`: segundos de espera por ping (default: `60`).
- `RECEPTORES`: correos separados por `;`.
- `SMTP_SERVER`: host SMTP.
- `SMTP_PORT`: puerto SMTP (ej. `587`).
- `SMTP_USER`: usuario SMTP.
- `SMTP_PASSWORD`: password SMTP.
- `SMTP_FROM_EMAIL`: remitente.
- `TEMPLATE_PATH`: ruta al HTML de la plantilla (ej. `./utils/templates/mail.html`).

## Ejecutar en local
1. `cp .env.example .env` y completa los valores.
2. `python main.py`

Si queres cargar `.env` automaticamente:
```bash
pip install python-dotenv
```

## Ejecutar con Docker
```bash
docker compose up --build
```

`compose.yaml` carga `.env` y monta `./utils/templates` dentro del contenedor.

## Plantilla de correo
- Archivo por defecto: `utils/templates/mail.html`
- Placeholder requerido: `{{SERVICIOS}}`

## Ejemplo de `.env`
```env
DOMINIOS=google.com;mrbot.com.ar;contadoresonline.com.ar
TIMEOUT=10
RECEPTORES=destinatario1@mail.com;destinatario2@mail.com
SMTP_SERVER=smtp.tu-servidor.com
SMTP_PORT=587
SMTP_USER=usuario
SMTP_PASSWORD=contraseña
SMTP_FROM_EMAIL=alertas@tudominio.com
TEMPLATE_PATH=./utils/templates/mail.html
```
