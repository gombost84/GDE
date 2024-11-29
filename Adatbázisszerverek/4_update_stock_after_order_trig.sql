-- Trigger a készlet frissítéséhez vásárláskor

CREATE TRIGGER UpdateStockAfterOrder
AFTER INSERT OR UPDATE ON OrderDetails
FOR EACH ROW
BEGIN
  -- A könyv készletének csökkentése a rendelési mennyiséggel
  UPDATE Books
  SET StockQuantity = StockQuantity - NEW.Quantity
  WHERE BookID = NEW.BookID;

  -- Elérhető-e még a könyv
  IF (SELECT StockQuantity FROM Books WHERE BookID = NEW.BookID) <= 0 THEN
    RAISE NOTICE 'Book % is out of stock.', NEW.BookID;
  END IF;
END;