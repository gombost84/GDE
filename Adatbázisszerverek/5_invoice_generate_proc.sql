-- Procedure számla automatikus készítéséhez

CREATE PROCEDURE GenerateInvoice(IN orderID INT)
LANGUAGE SQL
AS $$
BEGIN
  -- Létezik-e az OrderID
  IF NOT EXISTS (SELECT 1 FROM Orders WHERE OrderID = orderID) THEN
    RAISE EXCEPTION 'Order % does not exist.', orderID;
  END IF;

  -- A rendelés teljes ára
  DECLARE totalAmount MONEY;
  SELECT SUM(Quantity * Price) INTO totalAmount
  FROM OrderDetails
  WHERE OrderID = orderID;

  -- Számla létrehozása
  INSERT INTO Invoices (OrderID, InvoiceDate, TotalPrice, PaymentStatus)
  VALUES (orderID, NOW(), totalAmount, FALSE);
END;
$$;