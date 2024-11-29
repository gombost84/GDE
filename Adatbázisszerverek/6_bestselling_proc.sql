-- Procedure a 10 legjobban fogyó könyv lekérdezéséhez

CREATE PROCEDURE GetBestSellingBooks()
LANGUAGE SQL
AS $$
BEGIN
  SELECT Books.Title, SUM(OrderDetails.Quantity) AS TotalSold
  FROM OrderDetails
  JOIN Books ON OrderDetails.BookID = Books.BookID
  GROUP BY Books.Title
  ORDER BY TotalSold DESC
  LIMIT 10;
END;
$$;