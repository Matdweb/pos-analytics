USE [Northwind]

INSERT INTO DimDate (DateID, FullDate, Day, Month, Quarter, Year)
VALUES (99991231, '9999-12-31', 0, 0, 0, 0);


DECLARE @Fecha DATE = '2025-01-01';
DECLARE @Fin DATE = '2025-12-31';

-- Generar fechas para 2025, 2024 y 2023
WHILE @Fecha <= @Fin
BEGIN
    -- 2025
    INSERT INTO DimDate (DateID, FullDate, Day, Month, Quarter, Year)
    VALUES (
        CAST(FORMAT(@Fecha, 'yyyyMMdd') AS INT),
        @Fecha,
        DAY(@Fecha),
        MONTH(@Fecha),
        DATEPART(QUARTER, @Fecha),
        YEAR(@Fecha)
    );

    -- 2024
    INSERT INTO DimDate (DateID, FullDate, Day, Month, Quarter, Year)
    VALUES (
        CAST(FORMAT(DATEADD(YEAR, -1, @Fecha), 'yyyyMMdd') AS INT),
        DATEADD(YEAR, -1, @Fecha),
        DAY(DATEADD(YEAR, -1, @Fecha)),
        MONTH(DATEADD(YEAR, -1, @Fecha)),
        DATEPART(QUARTER, DATEADD(YEAR, -1, @Fecha)),
        YEAR(DATEADD(YEAR, -1, @Fecha))
    );

    -- 2023
    INSERT INTO DimDate (DateID, FullDate, Day, Month, Quarter, Year)
    VALUES (
        CAST(FORMAT(DATEADD(YEAR, -2, @Fecha), 'yyyyMMdd') AS INT),
        DATEADD(YEAR, -2, @Fecha),
        DAY(DATEADD(YEAR, -2, @Fecha)),
        MONTH(DATEADD(YEAR, -2, @Fecha)),
        DATEPART(QUARTER, DATEADD(YEAR, -2, @Fecha)),
        YEAR(DATEADD(YEAR, -2, @Fecha))
    );

    SET @Fecha = DATEADD(DAY, 1, @Fecha);
END