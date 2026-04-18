# MCP Gmail

Servidor MCP para conectar Claude Code con Gmail. Permite leer, buscar y enviar correos directamente desde Claude.

## Herramientas disponibles

| Herramienta | Descripción |
|-------------|-------------|
| `listar_correos` | Lista los últimos N correos de la bandeja de entrada |
| `buscar_correos` | Busca correos con la sintaxis de Gmail (`from:`, `subject:`, `is:unread`, etc.) |
| `leer_correo` | Lee el contenido completo de un correo por su ID |
| `enviar_correo` | Envía un correo a un destinatario |

## Instalación

### 1. Obtener credenciales de Google

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un proyecto nuevo (o usa uno existente)
3. Activa la **Gmail API**: APIs y servicios → Biblioteca → busca "Gmail API" → Activar
4. Crea credenciales OAuth 2.0: APIs y servicios → Credenciales → Crear credenciales → ID de cliente OAuth
   - Tipo de aplicación: **Aplicación de escritorio**
5. Descarga el archivo JSON y guárdalo como `credentials.json` dentro de esta carpeta (`mcp-gmail/`)

### 2. Instalar dependencias

```bash
cd mcp-gmail
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Primer inicio (autorización)

La primera vez se abrirá el navegador para que autorices el acceso a tu cuenta de Gmail:

```bash
python server.py
```

Esto genera un archivo `token.json` local que se reutiliza en los siguientes arranques.

### 4. Configurar en Claude Code

Añade esto a tu `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "python",
      "args": ["/ruta/absoluta/a/mcp-gmail/server.py"]
    }
  }
}
```

> Si usas el entorno virtual, reemplaza `python` por la ruta absoluta al Python del venv:
> `"/ruta/a/mcp-gmail/venv/bin/python"`

Reinicia Claude Code y el servidor estará disponible.
