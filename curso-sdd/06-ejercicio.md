# Módulo 06 — Ejercicio Completo: Sistema de Transferencias

Aplicarás todo lo aprendido construyendo un sistema de transferencias bancarias de principio a fin, siguiendo el ciclo SDD.

---

## El problema

El equipo de negocio te entrega esta descripción:

> "Necesitamos que los clientes puedan transferir dinero entre sus cuentas. El sistema debe validar que haya saldo suficiente, que el monto sea positivo y que ambas cuentas existan. Cada transferencia exitosa debe quedar registrada con fecha, monto y cuentas involucradas."

---

## Paso 1: Construir el lenguaje ubicuo

Del texto anterior extraemos:

| Término | Definición |
|---------|------------|
| **Cuenta** | Entidad con número único y saldo disponible |
| **Cliente** | Titular de una o más cuentas |
| **Transferencia** | Movimiento de dinero de una cuenta origen a una cuenta destino |
| **Saldo disponible** | Monto que puede ser debitado de una cuenta |
| **Registro de transferencia** | Evidencia inmutable de una transferencia realizada |

---

## Paso 2: Modelar el dominio

```python
# dominio/cuenta.py

from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass(frozen=True)
class Dinero:
    monto: float
    moneda: str = "CLP"

    def __post_init__(self):
        if self.monto < 0:
            raise ValueError("El monto no puede ser negativo")


@dataclass
class Transferencia:
    id: str
    cuenta_origen: str
    cuenta_destino: str
    monto: Dinero
    fecha: datetime = field(default_factory=datetime.now)
    estado: str = "completada"


class Cuenta:
    def __init__(self, numero: str, saldo_inicial: float):
        self.numero = numero
        self._saldo = saldo_inicial
        self._historial: List[Transferencia] = []

    @property
    def saldo(self) -> float:
        return self._saldo

    def debitar(self, dinero: Dinero) -> None:
        if dinero.monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        if dinero.monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= dinero.monto

    def acreditar(self, dinero: Dinero) -> None:
        if dinero.monto <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self._saldo += dinero.monto


class ServicioTransferencia:
    def __init__(self, repositorio_cuentas):
        self._repo = repositorio_cuentas
        self._transferencias: List[Transferencia] = []

    def transferir(self, numero_origen: str, numero_destino: str, monto: float) -> Transferencia:
        origen = self._repo.buscar(numero_origen)
        destino = self._repo.buscar(numero_destino)

        if origen is None:
            raise ValueError(f"La cuenta {numero_origen} no existe")
        if destino is None:
            raise ValueError(f"La cuenta {numero_destino} no existe")

        dinero = Dinero(monto)
        origen.debitar(dinero)
        destino.acreditar(dinero)

        transferencia = Transferencia(
            id=f"txn-{len(self._transferencias) + 1}",
            cuenta_origen=numero_origen,
            cuenta_destino=numero_destino,
            monto=dinero,
        )
        self._transferencias.append(transferencia)
        return transferencia
```

---

## Paso 3: Escribir las especificaciones

```gherkin
# features/transferencia.feature

Feature: Transferencia entre cuentas
  Como cliente del banco
  Quiero transferir dinero entre mis cuentas
  Para gestionar mi dinero sin ir a una sucursal

  Scenario: Transferencia exitosa
    Given que existe la cuenta "001" con saldo $1000
    And existe la cuenta "002" con saldo $500
    When transfiero $200 de la cuenta "001" a la cuenta "002"
    Then la transferencia debe ser exitosa
    And el saldo de la cuenta "001" debe ser $800
    And el saldo de la cuenta "002" debe ser $700
    And debe quedar un registro de la transferencia

  Scenario: Saldo insuficiente
    Given que existe la cuenta "001" con saldo $100
    And existe la cuenta "002" con saldo $0
    When intento transferir $200 de la cuenta "001" a la cuenta "002"
    Then debe rechazarse con el error "Saldo insuficiente"
    And el saldo de la cuenta "001" debe seguir siendo $100

  Scenario: Cuenta origen inexistente
    Given que existe la cuenta "002" con saldo $500
    When intento transferir $100 de la cuenta "999" a la cuenta "002"
    Then debe rechazarse con el error "La cuenta 999 no existe"

  Scenario: Monto cero
    Given que existe la cuenta "001" con saldo $500
    And existe la cuenta "002" con saldo $0
    When intento transferir $0 de la cuenta "001" a la cuenta "002"
    Then debe rechazarse con el error "El monto debe ser mayor a cero"

  Scenario Outline: Transferencias en el límite del saldo
    Given que existe la cuenta "001" con saldo $<saldo>
    And existe la cuenta "002" con saldo $0
    When intento transferir $<monto> de la cuenta "001" a la cuenta "002"
    Then el resultado debe ser "<resultado>"

    Examples:
      | saldo | monto | resultado |
      | 500   | 499   | exitosa   |
      | 500   | 500   | exitosa   |
      | 500   | 501   | rechazada |
```

---

## Paso 4: Escribir los steps

```python
# features/steps/transferencia_steps.py

from behave import given, when, then
from dominio.cuenta import Cuenta, ServicioTransferencia


class RepositorioCuentasEnMemoria:
    def __init__(self):
        self._cuentas = {}

    def guardar(self, cuenta: Cuenta):
        self._cuentas[cuenta.numero] = cuenta

    def buscar(self, numero: str):
        return self._cuentas.get(numero)


@given('que existe la cuenta "{numero}" con saldo ${saldo:d}')
def step_crear_cuenta(context, numero, saldo):
    if not hasattr(context, 'repo'):
        context.repo = RepositorioCuentasEnMemoria()
        context.servicio = ServicioTransferencia(context.repo)
    cuenta = Cuenta(numero, saldo)
    context.repo.guardar(cuenta)

@given('existe la cuenta "{numero}" con saldo ${saldo:d}')
def step_crear_cuenta_adicional(context, numero, saldo):
    step_crear_cuenta(context, numero, saldo)

@when('transfiero ${monto:d} de la cuenta "{origen}" a la cuenta "{destino}"')
def step_transferir(context, monto, origen, destino):
    context.error = None
    context.transferencia = None
    try:
        context.transferencia = context.servicio.transferir(origen, destino, monto)
    except ValueError as e:
        context.error = str(e)

@when('intento transferir ${monto:d} de la cuenta "{origen}" a la cuenta "{destino}"')
def step_intentar_transferir(context, monto, origen, destino):
    step_transferir(context, monto, origen, destino)

@then('la transferencia debe ser exitosa')
def step_transferencia_exitosa(context):
    assert context.error is None, f"Se esperaba éxito pero hubo error: {context.error}"
    assert context.transferencia is not None

@then('el saldo de la cuenta "{numero}" debe ser ${esperado:d}')
def step_verificar_saldo(context, numero, esperado):
    cuenta = context.repo.buscar(numero)
    assert cuenta.saldo == esperado, f"Esperado ${esperado}, actual ${cuenta.saldo}"

@then('el saldo de la cuenta "{numero}" debe seguir siendo ${esperado:d}')
def step_saldo_sin_cambio(context, numero, esperado):
    step_verificar_saldo(context, numero, esperado)

@then('debe quedar un registro de la transferencia')
def step_verificar_registro(context):
    assert context.transferencia.id is not None
    assert context.transferencia.estado == "completada"

@then('debe rechazarse con el error "{mensaje}"')
def step_error_esperado(context, mensaje):
    assert context.error is not None, "Se esperaba un error pero no ocurrió ninguno"
    assert mensaje in context.error, f"Error esperado: '{mensaje}', obtenido: '{context.error}'"

@then('el resultado debe ser "{resultado}"')
def step_resultado(context, resultado):
    if resultado == "exitosa":
        assert context.error is None, f"Se esperaba éxito: {context.error}"
    else:
        assert context.error is not None, "Se esperaba un rechazo pero fue exitosa"
```

---

## Paso 5: Ejecutar y verificar

```bash
# Estructura final del proyecto
proyecto/
├── features/
│   ├── transferencia.feature
│   └── steps/
│       └── transferencia_steps.py
└── dominio/
    └── cuenta.py

# Ejecutar
pip install behave
behave
```

Salida esperada:
```
Feature: Transferencia entre cuentas

  Scenario: Transferencia exitosa                        ✅ passed
  Scenario: Saldo insuficiente                           ✅ passed
  Scenario: Cuenta origen inexistente                    ✅ passed
  Scenario: Monto cero                                   ✅ passed
  Scenario Outline: Transferencias en el límite (x3)    ✅ passed

7 scenarios (7 passed)
28 steps (28 steps passed)
```

---

## Resumen del ciclo aplicado

```
Módulo 01  →  Entendiste qué es SDD y por qué importa
Módulo 02  →  Definiste el dominio: Cuenta, Dinero, Transferencia
Módulo 03  →  Escribiste specs ejecutables en Gherkin
Módulo 04  →  Conectaste specs con código (steps + dominio)
Módulo 05  →  Diseñaste el contrato de la API con OpenAPI
Módulo 06  →  Integraste todo en un proyecto funcional
```

## Próximos pasos sugeridos

- Agregar la capa API REST con **FastAPI** generando el OpenAPI automáticamente
- Conectar los tests Gherkin contra el servidor HTTP real usando `requests`
- Persistir las cuentas en base de datos reemplazando `RepositorioCuentasEnMemoria`
- Añadir autenticación y validar que un cliente solo transfiere desde sus propias cuentas
