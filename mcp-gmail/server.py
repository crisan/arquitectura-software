#!/usr/bin/env python3
import base64
import os
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_FILE = os.path.join(DIR, "credentials.json")
TOKEN_FILE = os.path.join(DIR, "token.json")

mcp = FastMCP("Gmail")


def _get_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)


def _decode_body(payload):
    if "parts" in payload:
        for part in payload["parts"]:
            if part["mimeType"] == "text/plain":
                data = part["body"].get("data", "")
                if data:
                    return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
    data = payload.get("body", {}).get("data", "")
    if data:
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
    return "(sin contenido de texto)"


def _headers_dict(msg):
    return {h["name"]: h["value"] for h in msg["payload"]["headers"]}


@mcp.tool()
def listar_correos(cantidad: int = 10) -> str:
    """Lista los últimos correos de la bandeja de entrada."""
    service = _get_service()
    result = (
        service.users()
        .messages()
        .list(userId="me", maxResults=cantidad, labelIds=["INBOX"])
        .execute()
    )
    messages = result.get("messages", [])
    if not messages:
        return "No hay correos en la bandeja de entrada."

    correos = []
    for msg in messages:
        detail = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=msg["id"],
                format="metadata",
                metadataHeaders=["From", "Subject", "Date"],
            )
            .execute()
        )
        h = _headers_dict(detail)
        correos.append(
            f"ID: {msg['id']}\n"
            f"De: {h.get('From', 'Desconocido')}\n"
            f"Asunto: {h.get('Subject', 'Sin asunto')}\n"
            f"Fecha: {h.get('Date', '')}"
        )
    return "\n---\n".join(correos)


@mcp.tool()
def buscar_correos(consulta: str, cantidad: int = 10) -> str:
    """Busca correos con la sintaxis de Gmail (ej: 'from:juan@gmail.com', 'subject:factura', 'is:unread')."""
    service = _get_service()
    result = (
        service.users()
        .messages()
        .list(userId="me", q=consulta, maxResults=cantidad)
        .execute()
    )
    messages = result.get("messages", [])
    if not messages:
        return f"No se encontraron correos para: '{consulta}'"

    correos = []
    for msg in messages:
        detail = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=msg["id"],
                format="metadata",
                metadataHeaders=["From", "Subject", "Date"],
            )
            .execute()
        )
        h = _headers_dict(detail)
        correos.append(
            f"ID: {msg['id']}\n"
            f"De: {h.get('From', 'Desconocido')}\n"
            f"Asunto: {h.get('Subject', 'Sin asunto')}\n"
            f"Fecha: {h.get('Date', '')}"
        )
    return "\n---\n".join(correos)


@mcp.tool()
def leer_correo(id_correo: str) -> str:
    """Lee el contenido completo de un correo dado su ID."""
    service = _get_service()
    msg = (
        service.users()
        .messages()
        .get(userId="me", id=id_correo, format="full")
        .execute()
    )
    h = _headers_dict(msg)
    cuerpo = _decode_body(msg["payload"])
    return (
        f"De: {h.get('From', 'Desconocido')}\n"
        f"Para: {h.get('To', 'Desconocido')}\n"
        f"Asunto: {h.get('Subject', 'Sin asunto')}\n"
        f"Fecha: {h.get('Date', '')}\n\n"
        f"{cuerpo}"
    )


@mcp.tool()
def enviar_correo(destinatario: str, asunto: str, cuerpo: str) -> str:
    """Envía un correo electrónico."""
    service = _get_service()
    mensaje = MIMEText(cuerpo)
    mensaje["to"] = destinatario
    mensaje["subject"] = asunto
    raw = base64.urlsafe_b64encode(mensaje.as_bytes()).decode()
    service.users().messages().send(userId="me", body={"raw": raw}).execute()
    return f"Correo enviado correctamente a {destinatario}."


if __name__ == "__main__":
    mcp.run()
