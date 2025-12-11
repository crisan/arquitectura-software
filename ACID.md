# ¿Que son las transacciones ACID?

Las transacciones ACID se refieren a cuatro propiedades que garantizan el procesamiento fiable de las transacciones de la base de datos. Los cuatro principios son:
- **A**tomicidad
- **C**onsistencia
- **I**solación
- **D**urabilidad

Estos principios garantizan que las transacciones se ejecuten completamente, sin actualizaciones parciales ni corrupción de datos. Las transacciones ACID son críticas en escenarios donde la integridad de los datos es primordial.

## Atomicidad
La atomicidad garantiza que una transacción se trate como una **unidad única e indivisible**. Esto significa que todas las operaciones de una transacción deben completarse o no completarse. Si falla alguna parte de la transacción, el sistema retrocede toda la transacción, garantizando que no se produzcan actualizaciones parciales.

**Ejemplo**: En una transacción bancaria, la atomicidad garantiza que ambas operaciones se completen con éxito cuando se descuenta en una cuenta y se abona en otra. Si falla el cargo o el abono, la operación se anula por completo.

## Coherencia
La coherencia garantiza que la transacción lleve a la base de datos de un estado válido a otro válido, respetando unas reglas y restricciones predifinidas. Tras completar una transacción, los datos deben cumplir todas las reglas de integridad de la base de datos.

**Ejemplo 1**: En banca, la coherencia garantiza que el saldo total de todas las cuentas permanece invariable tras una transferencia. Por ejemplo, si se transfieren $100 entre cuentas, la suma de los montos entre ambas cuentas debe seguir siendo $100. La **Coherencia** define el requisito y la **Atomicidad** proporciona el mecanismo para restaurarlo. 

**Ejemplo 2**: 
| Estado | Saldo A | Saldo B | Regla de Coherencia | Válido/Inválido |
| -- | -- | -- | -- | -- |
| Inicial | $3000 | $4000 |  Suma Total = $7000 | ✅ Válido |
| Paso 1: Retiro Saldo A | $2000 | $4000 |  Suma Total = $6000 | ❌ Inválido |
| Paso 2: Abono Saldo B | $2000 | $5000 |  Suma Total = $7000 | ✅ Válido |

Si el sistema falla en el paso 1, la propiedad de **Atomicidad** asegura que se haga el rollback al estado **Inicial**  ($3000/$4000) manteniendo la **Coherencia** (Suma Total = $7000). La Coherencia define el requisito y la Atomocidad proporciona el mecanismo para restaurarlo.

## Aislamiento
El aislamiento que las transacciones interfieran entre sí. Cuando se ejecutan varias transacciones simultáneamente, el aislamiento garantiza que no afecten a los resultados de las demas. Cada transacción debe estar aislada para evitar conflictos, especialmente en entornos de alta concurrencia.

**Ejemplo**: Si dos clientes intentan comprar el último artículo en stock al mismo tiempo, el aislamiento garantiza que solo una transacción tendrá éxito y el inventario se actualizará correctamente para reflejar el cambio.
