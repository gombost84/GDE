-- Adott ügyfél vásárlásainak lekérdezése

select Orders.OrderID, OrderDate, TotalPrice, Books.Title, Books.Price, OrderDetails.Quantity 
from Orders
join OrderDetails on Orders.OrderID = OrderDetails.OrderID
join Books on OrderDetails.BookID = Books.BookID
where Orders.CustomerID = 1;

-- Könyvek készlete

select Title, StockQuantity 
from Books 
where StockQuantity > 0;

-- Adott ügyfél vásárlási előzményei

select OrderID, Status 
from Orders 
where CustomerID = 1;

-- Adott rendelés státusza

select OrderID, Status
from Orders
where OrderID = 1;

-- Adott rendelés részletei

select OrderDate, OrderDetails.BookID, Books.Title
from Orders
join OrderDetails on Orders.OrderID = OrderDetails.OrderID
join Books on OrderDetails.BookID = Books.BookID
where Orders.OrderID = 1;