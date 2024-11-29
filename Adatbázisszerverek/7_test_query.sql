-- Összetett lekérdezés a legutóbbi vásárlásokról és könyvekről

SELECT 
  Customers.Name,
  Orders.OrderDate,
  Books.Title,
  OrderDetails.Quantity
FROM 
  Customers
JOIN 
  Orders ON Customers.CustomerID = Orders.CustomerID
JOIN 
  OrderDetails ON Orders.OrderID = OrderDetails.OrderID
JOIN 
  Books ON OrderDetails.BookID = Books.BookID
WHERE 
  Orders.OrderDate >= NOW() - interval '30 days'
ORDER BY 
  Orders.OrderDate DESC;