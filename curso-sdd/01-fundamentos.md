# Módulo 01 — Fundamentos de SDD

## ¿Qué es Specification-Driven Development?

**SDD** es una metodología donde las **especificaciones** son el punto de partida del desarrollo. Antes de escribir código o tests, el equipo acuerda en texto legible *qué debe hacer* el sistema, *bajo qué condiciones* y *cuál es el resultado esperado*.

La especificación no es un documento PDF que nadie lee — es un artefacto vivo, ejecutable, que se convierte en tests automáticos.

---

## El problema que resuelve

En el desarrollo tradicional, el flujo es:

```
Reunión → Código → "¿Esto era lo que querías?" → Rehacer
```

Con SDD el flujo es:

```
Especificación acordada → Código → Tests pasan → Listo
```

El retrabajo se elimina porque el equipo (negocio + desarrollo) acuerda el comportamiento **antes** de construir.

---

## SDD vs TDD vs BDD

| Concepto | Quién lo escribe | Qué especifica | Legible por negocio |
|----------|-----------------|----------------|---------------------|
| **TDD** (Test-Driven Dev) | Desarrollador | Implementación técnica | No |
| **BDD** (Behavior-Driven Dev) | Desarrollador + QA | Comportamiento del sistema | Parcialmente |
| **SDD** (Specification-Driven Dev) | Negocio + Desarrollador | Qué debe hacer el sistema | Sí |

> SDD no reemplaza a TDD ni BDD — los envuelve. Las especificaciones SDD se convierten en los tests BDD, que guían el TDD.

---

## Los tres pilares de SDD

### 1. Especificación primero
Nadie escribe código sin una especificación aprobada. La spec responde: *¿qué problema resuelve esto?*

### 2. Lenguaje ubicuo
El equipo técnico y el de negocio usan las **mismas palabras** para describir el sistema. Si negocio dice "transferencia" y el código dice "payment_transaction", hay un problema.

### 3. Especificaciones ejecutables
Las especificaciones no son documentos — son tests. Si el comportamiento cambia, la spec cambia y los tests fallan.

---

## El ciclo SDD

```
1. ESPECIFICAR  →  Escribir el comportamiento esperado en lenguaje natural estructurado
2. CONFIRMAR    →  Negocio y desarrollo validan que la spec es correcta
3. AUTOMATIZAR  →  Convertir la spec en un test ejecutable
4. IMPLEMENTAR  →  Escribir el código mínimo para que el test pase
5. REFACTORIZAR →  Limpiar sin romper los tests
```

---

## Ejercicio 01

Piensa en un proceso que conozcas bien (alta de usuario, compra de producto, aprobación de crédito). Escribe en una oración:

- **Dado** que... (el contexto)
- **Cuando** ... (la acción)
- **Entonces** ... (el resultado esperado)

Ejemplo:
> *Dado que* un usuario tiene saldo suficiente,  
> *Cuando* realiza una transferencia de $100,  
> *Entonces* su saldo disminuye en $100 y el destinatario recibe $100.

Esto es el núcleo de una especificación. En el siguiente módulo construiremos el dominio alrededor de estas ideas.
