USE [Northwind];

SELECT 
    dc.Country AS CustomerCountry,
    dd.Year,
    SUM(fs.TotalAmount) AS TotalSales
FROM FactSales fs
JOIN DimCustomer dc ON fs.CustomerID = dc.CustomerID
JOIN DimDate dd ON fs.DateID = dd.DateID
GROUP BY dc.Country, dd.Year
ORDER BY dd.Year, TotalSales DESC;

SELECT 
    dp.ProductName,
    SUM(fs.Quantity) AS TotalQuantitySold
FROM FactSales fs
JOIN DimProduct dp ON fs.ProductID = dp.ProductID
GROUP BY dp.ProductName
ORDER BY TotalQuantitySold DESC;

SELECT 
    de.EmployeeName,
    de.Region,
    SUM(fs.TotalAmount) AS TotalSales
FROM FactSales fs
JOIN DimEmployee de ON fs.EmployeeID = de.EmployeeID
GROUP BY de.EmployeeName, de.Region
ORDER BY TotalSales DESC;

SELECT 
    dp.Category,
    AVG(fs.Discount) AS AvgDiscount
FROM FactSales fs
JOIN DimProduct dp ON fs.ProductID = dp.ProductID
GROUP BY dp.Category
ORDER BY AvgDiscount DESC;

SELECT 
    ds.SupplierName,
    dd.Month,
    dd.Year,
    SUM(fs.TotalAmount) AS MonthlySales
FROM FactSales fs
JOIN DimSupplier ds ON fs.SupplierID = ds.SupplierID
JOIN DimDate dd ON fs.DateID = dd.DateID
GROUP BY ds.SupplierName, dd.Year, dd.Month
ORDER BY ds.SupplierName, dd.Year, dd.Month;
