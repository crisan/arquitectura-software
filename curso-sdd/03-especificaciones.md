# Módulo 03 — Escribir Especificaciones con Gherkin

## ¿Qué es Gherkin?

**Gherkin** es el lenguaje estructurado que usamos para escribir especificaciones ejecutables. Es legible por humanos y procesable por herramientas como **Behave** (Python) o **Cucumber** (Java/JS).

Un archivo Gherkin se llama **feature** y tiene extensión `.feature`.

---

## Estructura básica

```gherkin
Feature: Nombre de la funcionalidad
  Descripción opcional de para qué sirve.

  Scenario: Nombre del escenario
    Given  <contexto inicial>
    When   <acción que ocurre>
    Then   <resultado esperado>
```

### Palabras clave

| Palabra | Significado |
|---------|-------------|
| `Feature` | Funcionalidad que se está especificando |
| `Scenario` | Un caso concreto de uso |
| `Given` | El estado del sistema antes de la acción |
| `When` | La acción que el usuario o sistema realiza |
| `Then` | Lo que debe ocurrir como resultado |
| `And` | Continúa el paso anterior (Given, When o Then) |
| `But` | Excepción o condición negativa |

---

## Ejemplo completo: Transferencia bancaria

```gherkin
Feature: Transferencia entre cuentas
  Como cliente del banco
  Quiero transferir dinero a otra cuenta
  Para pagar mis deudas sin ir a una sucursal

  Scenario: Transferencia exitosa con saldo suficiente
    Given que la cuenta "001" tiene un saldo de $500
    And la cuenta "002" tiene un saldo de $200
    When el cliente transfiere $100 desde la cuenta "001" a la cuenta "002"
    Then el saldo de la cuenta "001" debe ser $400
    And el saldo de la cuenta "002" debe ser $300

  Scenario: Transferencia rechazada por saldo insuficiente
    Given que la cuenta "001" tiene un saldo de $50
    When el cliente intenta transferir $100 desde la cuenta "001" a la cuenta "002"
    Then la transferencia debe ser rechazada
    And el saldo de la cuenta "001" debe seguir siendo $50

  Scenario: Transferencia rechazada por monto negativo
    Given que la cuenta "001" tiene un saldo de $500
    When el cliente intenta transferir $-50 desde la cuenta "001" a la cuenta "002"
    Then la transferencia debe ser rechazada con el error "El monto debe ser mayor a cero"
```

---

## Scenario Outline: múltiples casos

Cuando un escenario se repite con distintos datos, usa `Scenario Outline` con una tabla `Examples`:

```gherkin
  Scenario Outline: Transferencias con distintos montos
    Given que la cuenta origen tiene un saldo de $<saldo_origen>
    When el cliente transfiere $<monto>
    Then el resultado debe ser "<resultado>"

    Examples:
      | saldo_origen | monto | resultado  |
      | 500          | 100   | exitosa    |
      | 500          | 500   | exitosa    |
      | 500          | 501   | rechazada  |
      | 500          | 0     | rechazada  |
```

---

## Buenas prácticas al escribir specs

### Habla del comportamiento, no de la implementación

❌ Mal:
```gherkin
When se ejecuta el método "debitar(100)" en el objeto Cuenta
Then la variable "_saldo" debe valer 400
```

✅ Bien:
```gherkin
When el cliente transfiere $100
Then su saldo debe ser $400
```

### Un escenario = un comportamiento

Cada escenario debe probar **una sola cosa**. Si necesitas verificar dos comportamientos distintos, escribe dos escenarios.

### Usa el lenguaje ubicuo

Las palabras en los escenarios deben coincidir exactamente con el glosario del dominio definido en el Módulo 02.

### Los escenarios son independientes

Cada escenario debe poder ejecutarse solo, sin depender del estado que dejó otro escenario.

---

## Ejercicio 03

Toma el proceso del Ejercicio 01 y escribe al menos **3 escenarios Gherkin**:

1. El camino feliz (todo sale bien)
2. El error más común (ej: saldo insuficiente, datos inválidos)
3. Un caso borde (ej: transferir exactamente el saldo disponible, monto cero)

Guarda el archivo como `mi-proceso.feature`. En el siguiente módulo lo convertiremos en tests ejecutables.
