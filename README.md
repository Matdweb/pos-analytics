# Scripts SQL del Proyecto Data Warehouse

Este directorio contiene los scripts necesarios para crear y poblar el Data Warehouse del proyecto.

## Archivos incluidos

- `01_dim_cliente.sql`: Crea la dimensión cliente.
- `02_dim_producto.sql`: Crea la dimensión producto.
- `03_fact_ventas.sql`: Crea la tabla de hechos de ventas.
- `04_insert_datos.sql`: Inserta datos de prueba.

## Instrucciones

1. Abre SQL Server Management Studio (SSMS).
2. Conéctate a tu instancia de SQL Server.
3. Ejecuta cada script en el siguiente orden:
    - `01_dim_cliente.sql`
    - `02_dim_producto.sql`
    - `03_fact_ventas.sql`
    - `04_insert_datos.sql`
