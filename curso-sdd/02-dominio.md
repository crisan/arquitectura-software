# Módulo 02 — Modelar el Dominio

## ¿Qué es el dominio?

El **dominio** es el problema del mundo real que el software resuelve. En un banco, el dominio incluye cuentas, transferencias, saldos, clientes. En un e-commerce, incluye productos, carritos, pedidos, envíos.

Modelar el dominio correctamente es lo que hace que las especificaciones tengan sentido para todos.

---

## Lenguaje ubicuo (Ubiquitous Language)

El **lenguaje ubicuo** es un vocabulario compartido entre el equipo técnico y el negocio. Cada concepto del dominio tiene un nombre único que se usa en:

- Las conversaciones
- Las especificaciones
- El código
- La base de datos

### Ejemplo de problema

| Negocio dice | Desarrollador dice | Base de datos tiene |
|-------------|-------------------|---------------------|
| "Transferencia" | `PaymentTransaction` | tabla `mov_fin` |
| "Cliente" | `User` | tabla `tbl_usr` |
| "Saldo disponible" | `balance` | columna `amt_avail` |

Este desacople genera bugs silenciosos y malentendidos. El lenguaje ubicuo los elimina.

### Cómo construirlo

1. Reúne a una persona de negocio y una técnica
2. Haz que negocio describa el proceso en voz alta
3. Extrae los sustantivos (entidades) y los verbos (acciones)
4. Acuerda un nombre único para cada uno
5. Úsalo en todas partes sin excepción

---

## Entidades y Objetos de Valor

### Entidad
Una **entidad** tiene identidad propia. Dos instancias con los mismos datos son objetos distintos si tienen distinto ID.

**Ejemplo**: Dos cuentas bancarias con saldo $1.000 son cuentas distintas — tienen distinto número de cuenta.

```python
class Cuenta:
    def __init__(self, numero: str, saldo: float):
        self.numero = numero   # identidad
        self.saldo = saldo
```

### Objeto de Valor
Un **objeto de valor** no tiene identidad. Dos instancias con los mismos datos son intercambiables.

**Ejemplo**: $100 es $100 — no importa qué billete específico sea.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Dinero:
    monto: float
    moneda: str  # "CLP", "USD"
```

---

## Bounded Context (Contexto Delimitado)

Un **bounded context** es el límite dentro del cual un modelo de dominio es válido y consistente. Fuera de ese límite, los mismos términos pueden tener otro significado.

### Ejemplo

En un banco el término "cliente" significa cosas distintas según el contexto:

| Contexto | Qué es un "cliente" |
|----------|---------------------|
| **Cuentas** | Titular con RUT, nombre, cuentas asociadas |
| **Riesgo** | Entidad con historial crediticio y score |
| **Marketing** | Segmento con preferencias y campañas asignadas |

Cada contexto tiene su propio modelo. No se fuerza un modelo único para todos.

---

## Agregados y Raíz de Agregado

Un **agregado** es un grupo de entidades y objetos de valor que se tratan como una unidad. La **raíz del agregado** es la única entidad a través de la cual se accede al resto.

**Ejemplo**: Una `Cuenta` es la raíz del agregado. Para modificar el saldo, siempre pasas por `Cuenta`, nunca modificas el saldo directamente.

```python
class Cuenta:
    def __init__(self, numero: str, saldo_inicial: float):
        self.numero = numero
        self._saldo = saldo_inicial
        self._movimientos = []

    def debitar(self, monto: float):
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente")
        self._saldo -= monto
        self._movimientos.append(Movimiento("DEBITO", monto))

    def acreditar(self, monto: float):
        self._saldo += monto
        self._movimientos.append(Movimiento("CREDITO", monto))

    @property
    def saldo(self):
        return self._saldo
```

---

## Ejercicio 02

Toma el proceso que describiste en el Ejercicio 01 e identifica:

1. **Lenguaje ubicuo**: 3 términos clave del dominio con su definición acordada
2. **Entidades**: qué objetos tienen identidad propia (necesitan un ID)
3. **Objetos de valor**: qué objetos son intercambiables si tienen los mismos datos
4. **Bounded context**: ¿en qué contexto aplica tu proceso?

En el siguiente módulo tomaremos estos elementos y escribiremos especificaciones ejecutables.
