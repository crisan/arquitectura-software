# Módulo 05 — SDD con APIs REST (API-First)

## ¿Qué es API-First?

**API-First** es la aplicación de SDD al diseño de APIs: primero defines el contrato de la API en OpenAPI, lo validas con el equipo, y *luego* implementas el servidor.

```
OpenAPI spec  →  Mock server  →  Tests de contrato  →  Implementación
```

Beneficios:
- El equipo frontend puede trabajar contra el mock mientras backend implementa
- El contrato es la fuente de verdad, no el código
- Los cambios de API se discuten en la spec antes de romper clientes

---

## Estructura de un archivo OpenAPI

```yaml
# transferencias.yaml

openapi: "3.0.3"
info:
  title: API de Transferencias
  version: "1.0"

paths:
  /transferencias:
    post:
      summary: Realizar una transferencia entre cuentas
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SolicitudTransferencia'
      responses:
        "201":
          description: Transferencia realizada correctamente
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Transferencia'
        "422":
          description: Saldo insuficiente o datos inválidos
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'

components:
  schemas:
    SolicitudTransferencia:
      type: object
      required: [cuenta_origen, cuenta_destino, monto]
      properties:
        cuenta_origen:
          type: string
          example: "001"
        cuenta_destino:
          type: string
          example: "002"
        monto:
          type: number
          minimum: 0.01
          example: 100.00

    Transferencia:
      type: object
      properties:
        id:
          type: string
          example: "txn-abc123"
        cuenta_origen:
          type: string
        cuenta_destino:
          type: string
        monto:
          type: number
        estado:
          type: string
          enum: [completada, rechazada]
        fecha:
          type: string
          format: date-time

    Error:
      type: object
      properties:
        codigo:
          type: string
          example: "SALDO_INSUFICIENTE"
        mensaje:
          type: string
          example: "El saldo disponible es insuficiente para esta transferencia"
```

---

## Levantar un mock server con Prism

**Prism** lee tu OpenAPI y levanta un servidor que responde con datos de ejemplo — sin escribir código.

```bash
npm install -g @stoplight/prism-cli
prism mock transferencias.yaml
```

Ahora puedes hacer peticiones reales:

```bash
curl -X POST http://localhost:4010/transferencias \
  -H "Content-Type: application/json" \
  -d '{"cuenta_origen":"001","cuenta_destino":"002","monto":100}'
```

El frontend ya puede trabajar mientras tú implementas el backend.

---

## Tests de contrato con Schemathesis

**Schemathesis** genera y ejecuta tests automáticamente a partir de tu OpenAPI, verificando que la implementación respeta el contrato.

```bash
pip install schemathesis
schemathesis run transferencias.yaml --url http://localhost:8000
```

Schemathesis prueba automáticamente:
- Que los códigos de respuesta coinciden con la spec
- Que los esquemas de respuesta son válidos
- Casos borde (valores nulos, strings vacíos, números negativos)

---

## Conectar OpenAPI con Gherkin

La especificación OpenAPI describe el *contrato*. Los escenarios Gherkin describen el *comportamiento*. Se complementan:

```gherkin
Feature: Transferencia via API

  Scenario: Transferencia exitosa
    Given que existe una cuenta "001" con saldo $500
    And existe una cuenta "002" con saldo $200
    When se envía POST /transferencias con monto $100 de "001" a "002"
    Then la respuesta debe ser 201
    And el cuerpo debe contener estado "completada"
    And la cuenta "001" debe tener saldo $400

  Scenario: Saldo insuficiente
    Given que existe una cuenta "001" con saldo $50
    When se envía POST /transferencias con monto $100 de "001" a "002"
    Then la respuesta debe ser 422
    And el cuerpo debe contener codigo "SALDO_INSUFICIENTE"
```

---

## Flujo API-First completo

```
1. Escribe el OpenAPI  →  Revisión con el equipo
2. Levanta mock Prism  →  Frontend empieza a integrar
3. Escribe specs Gherkin vinculadas al contrato
4. Ejecuta Schemathesis →  Verifica que la impl respeta el contrato
5. Implementa el servidor  →  Los tests deben pasar
6. Si necesitas cambiar la API  →  Cambia primero el OpenAPI, luego el código
```

---

## Ejercicio 05

Toma tu proceso del Ejercicio 01 y diseña el contrato de su API:

1. Escribe el archivo `mi-proceso.yaml` con al menos un endpoint
2. Define los esquemas de request y response
3. Incluye al menos dos respuestas: éxito y error
4. Levanta el mock con Prism y prueba el endpoint con `curl`

En el módulo final integraremos todo en un proyecto completo.
