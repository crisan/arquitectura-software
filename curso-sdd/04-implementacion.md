# Módulo 04 — De Especificación a Código

## El ciclo completo

```
.feature  →  steps.py  →  dominio.py
(spec)       (glue)        (código)
```

1. **`.feature`** — La especificación Gherkin (ya la tienes del Módulo 03)
2. **`steps.py`** — El "pegamento" que conecta cada paso Gherkin con código Python
3. **`dominio.py`** — El código real que implementa el comportamiento

La regla es: **nunca escribas código de dominio sin que exista un step que lo llame y una spec que lo describa.**

---

## Herramienta: Behave

**Behave** es el framework de BDD para Python que ejecuta archivos `.feature`.

```bash
pip install behave
```

Estructura de carpetas:

```
proyecto/
├── features/
│   ├── transferencia.feature    ← especificaciones
│   └── steps/
│       └── transferencia_steps.py  ← glue code
└── dominio/
    └── cuenta.py                ← código de dominio
```

---

## Paso 1: La especificación (ya conocida)

```gherkin
# features/transferencia.feature

Feature: Transferencia entre cuentas

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
```

---

## Paso 2: Los steps (glue code)

```python
# features/steps/transferencia_steps.py

from behave import given, when, then
from dominio.cuenta import Cuenta, ServicioTransferencia

@given('que la cuenta "{numero}" tiene un saldo de ${saldo:d}')
def step_crear_cuenta(context, numero, saldo):
    if not hasattr(context, 'cuentas'):
        context.cuentas = {}
    context.cuentas[numero] = Cuenta(numero, saldo)

@when('el cliente transfiere ${monto:d} desde la cuenta "{origen}" a la cuenta "{destino}"')
def step_transferir(context, monto, origen, destino):
    context.error = None
    try:
        servicio = ServicioTransferencia()
        servicio.transferir(
            context.cuentas[origen],
            context.cuentas[destino],
            monto
        )
    except ValueError as e:
        context.error = str(e)

@when('el cliente intenta transferir ${monto:d} desde la cuenta "{origen}" a la cuenta "{destino}"')
def step_intentar_transferir(context, monto, origen, destino):
    step_transferir(context, monto, origen, destino)

@then('el saldo de la cuenta "{numero}" debe ser ${saldo_esperado:d}')
def step_verificar_saldo(context, numero, saldo_esperado):
    assert context.cuentas[numero].saldo == saldo_esperado, (
        f"Esperado ${saldo_esperado}, obtenido ${context.cuentas[numero].saldo}"
    )

@then('la transferencia debe ser rechazada')
def step_transferencia_rechazada(context):
    assert context.error is not None, "Se esperaba un error pero la transferencia fue exitosa"

@then('el saldo de la cuenta "{numero}" debe seguir siendo ${saldo_esperado:d}')
def step_saldo_sin_cambios(context, numero, saldo_esperado):
    step_verificar_saldo(context, numero, saldo_esperado)
```

---

## Paso 3: El código de dominio

Ahora escribes el **mínimo código necesario** para que los tests pasen:

```python
# dominio/cuenta.py

class Cuenta:
    def __init__(self, numero: str, saldo_inicial: float):
        self.numero = numero
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def debitar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= monto

    def acreditar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self._saldo += monto


class ServicioTransferencia:
    def transferir(self, origen: Cuenta, destino: Cuenta, monto: float):
        origen.debitar(monto)   # si falla aquí, destino no se toca (Atomicidad)
        destino.acreditar(monto)
```

---

## Paso 4: Ejecutar los tests

```bash
behave features/transferencia.feature
```

Salida esperada:

```
Feature: Transferencia entre cuentas

  Scenario: Transferencia exitosa con saldo suficiente   ✅ passed
  Scenario: Transferencia rechazada por saldo insuficiente  ✅ passed

2 scenarios (2 passed)
6 steps (6 passed)
```

---

## La regla de oro: Red → Green → Refactor

1. **Red**: Ejecuta los tests antes de escribir el código → deben fallar
2. **Green**: Escribe el mínimo código para que pasen
3. **Refactor**: Mejora el código sin romper los tests

Si los tests ya pasan antes de escribir código, la especificación no estaba probando nada nuevo.

---

## Ejercicio 04

Con los escenarios que escribiste en el Ejercicio 03:

1. Crea la estructura de carpetas `features/` y `features/steps/`
2. Escribe los steps que conectan cada paso Gherkin con código Python
3. Ejecuta `behave` — verifica que fallen (Red)
4. Escribe el código de dominio mínimo para que pasen (Green)
5. Refactoriza si hay duplicación o el código no es claro

En el siguiente módulo aplicamos SDD a una API REST real.
