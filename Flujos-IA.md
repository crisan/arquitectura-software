# Flujos IA #

Documento de trabajo para registrar flujos de trabajo asistidos por IA: qué tarea se automatiza, cómo se orquesta y qué criterios de calidad se aplican.

## Objetivo ##

Describir flujos de trabajo con IA de forma reproducible, para que puedan revisarse, mejorarse y adoptarse por otros equipos.

## Estructura de cada flujo ##

Cada flujo debería documentar:

- **Propósito**: problema concreto que resuelve.
- **Entradas y salidas**: qué información recibe y qué produce.
- **Pasos**: secuencia de llamadas a modelos, herramientas o revisiones humanas.
- **Puntos de control humano**: dónde una persona aprueba o corrige antes de continuar.
- **Criterios de éxito**: cómo se mide que el flujo funciona.
- **Riesgos**: datos sensibles, alucinaciones, dependencia de proveedor, costo.

**Ejemplo**: flujo de redacción de ADRs asistida por IA.

1. Entrada: descripción en lenguaje natural de la decisión y su contexto.
2. Paso IA: generar un borrador con la estructura de ADR (contexto, alternativas, consecuencias).
3. Punto de control: el arquitecto revisa alternativas descartadas y justificación.
4. Salida: ADR versionado en el repositorio.
5. Criterio de éxito: el ADR se aprueba sin reescribir las alternativas.

## Flujos documentados ##

- _Pendiente_: añadir los primeros flujos.
