# Server Status Check

Este proyecto permite **monitorear dominios/servicios** mediante pings periódicos y, en caso de detectar fallas, **enviar alertas por correo electrónico** con un template HTML personalizado.

## 📂 Estructura del proyecto

```
.
├── main.py              # Script principal: chequea dominios y dispara alertas
├── utils/
│   └── email.py         # Funciones para enviar correos y generar el cuerpo HTML
├── mail.html            # Template HTML del correo de alerta
├── Dockerfile           # Imagen base para contenerizar la app
├── compose.yaml         # Definición de servicio en Docker Compose
├── .env.example         # Variables de entorno de ejemplo
├── .dockerignore        # Exclusiones para la imagen Docker
├── .gitignore           # Exclusiones para Git
```

## ⚙️ Configuración

El proyecto se basa en variables de entorno definidas en un archivo `.env`.  
Ejemplo (`.env.example`):

```ini
# Configuración de dominios a monitorear (separados por ;)
DOMINIOS=google.com;mrbot.com.ar;contadoresonline.com.ar

# Lista de correos receptores (separados por ;)
RECEPTORES=destinatario1@mail.com;destinatario2@mail.com

# Configuración SMTP
SMTP_SERVER=smtp.tu-servidor.com
SMTP_PORT=587
SMTP_USER=usuario
SMTP_PASSWORD=contraseña
SMTP_FROM_EMAIL=alertas@tudominio.com

# Ruta al template HTML del correo
TEMPLATE_PATH=utils/templates/mail.html
```

⚠️ Recuerda **copiar `.env.example` a `.env`** y completar tus credenciales.

## 🚀 Uso

### 1. Ejecutar localmente

Requisitos:
- Python 3.9+
- Librerías estándar (no requiere dependencias externas)

Ejecutar:

```bash
python main.py
```

### 2. Usar con Docker

Construir la imagen:

```bash
docker build -t server-status-check .
```

Levantar con Docker Compose:

```bash
docker compose up -d
```

El servicio definido en `compose.yaml` monta automáticamente el directorio de templates y carga variables desde `.env`.

## 📧 Funcionamiento del envío de correos

1. `main.py` hace ping a cada dominio listado en `DOMINIOS`.
2. Si alguno falla, se genera un cuerpo HTML a partir de `mail.html`.
3. El correo se envía a todos los receptores definidos en `RECEPTORES` mediante `SMTP_SERVER`.

Ejemplo de alerta recibida:

> **FALLA EN SERVICIOS (2)**  
> Se detectaron fallas en los siguientes servicios:
> - google.com  
> - mrbot.com.ar  

Con diseño HTML estilizado y logo embebido.

## 📦 Extensiones posibles

- Programar la ejecución periódica con **cron** o **supervisord**.
- Agregar más validaciones (ej. HTTP status code).
- Integrar con servicios de monitoreo externos.

---

👨‍💻 Desarrollado por [Agustín Bustos Piasentini](https://www.linkedin.com/in/agust%C3%ADn-bustos-piasentini-468446122/)  
🔗 Proyecto de ejemplo para monitoreo y alertas automáticas.