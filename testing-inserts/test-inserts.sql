USE [Northwind];

INSERT INTO dbo.Customers (CustomerID, CompanyName, ContactName, City, Country) VALUES ('CUST0935', 'Bennett-Quin', 'Linda Jenkins', 'North Shrewsbury', 'France');
INSERT INTO dbo.Products (ProductName, SupplierID, CategoryID, UnitPrice) VALUES ('Product 168', 11, 8, 477.55);
INSERT INTO dbo.Orders (CustomerID, EmployeeID, OrderDate, ShipVia) VALUES('CUST0026', 11, '2022-12-18', 3);
INSERT INTO dbo.[Order Details] (OrderID, ProductID, UnitPrice, Quantity, Discount) VALUES (4, 51, 104.76, 7, 0.18);

dbcc CHECKIDENT ('Orders', RESEED, 0);
dbcc CHECKIDENT ('Products', RESEED, 0);
dbcc CHECKIDENT ('Employees', RESEED, 0);
dbcc CHECKIDENT ('FactSales', RESEED, 0);