USE Northwind;

-- TABLA DE HECHOS
CREATE TABLE FactSales (
    SalesID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT,
    CustomerID NCHAR(8),
    EmployeeID INT,
    SupplierID INT,
    DateID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    Discount DECIMAL(5,2),
    TotalAmount AS (Quantity * UnitPrice * (1 - Discount)),
    FOREIGN KEY (ProductID) REFERENCES DimProduct(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES DimCustomer(CustomerID),
    FOREIGN KEY (EmployeeID) REFERENCES DimEmployee(EmployeeID),
    FOREIGN KEY (SupplierID) REFERENCES DimSupplier(SupplierID),
    FOREIGN KEY (DateID) REFERENCES DimDate(DateID),
);

SELECT * FROM FactSales;

-- TABLAS DE DIMENSIÓN

CREATE TABLE DimSupplier (
    SupplierID INT PRIMARY KEY,
    SupplierName NVARCHAR(100),
    Country NVARCHAR(100)
);

SELECT * FROM DimSupplier;

CREATE TABLE DimProduct (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Category NVARCHAR(50),
    SupplierName NVARCHAR(100),
);

SELECT * FROM DimProduct;

CREATE TABLE DimCustomer (
    CustomerID NCHAR(8) PRIMARY KEY,
    CustomerName NVARCHAR(100),
    City NVARCHAR(100),
    Country NVARCHAR(100)
);

SELECT * FROM DimCustomer;

CREATE TABLE DimEmployee (
    EmployeeID INT PRIMARY KEY,
    EmployeeName NVARCHAR(100),
    Title NVARCHAR(50),
    Region NVARCHAR(50)
);

SELECT * FROM DimEmployee;

CREATE TABLE DimDate (
    DateID INT PRIMARY KEY,
    FullDate DATE,
    Day INT,
    Month INT,
    Quarter INT,
    Year INT
);

SELECT * FROM DimDate;