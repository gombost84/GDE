insert into Books (BookID, Title, Authors, ISBN, LangCode, PubDate, Publisher, StockQuantity, Price)
values
(1, 'Harry Potter and the Half-Blood Prince (Harry Potter  #6)', 'J.K. Rowling/Mary GrandPré', '439785960', 'eng', '2006.09.16', 'Scholastic Inc.', 19, 5000),
(2, 'Harry Potter and the Order of the Phoenix (Harry Potter  #5)', 'J.K. Rowling/Mary GrandPré', '439358078', 'eng', '2004.09.01', 'Scholastic Inc.', 17, 5000),
(3, 'Harry Potter and the Chamber of Secrets (Harry Potter  #2)', 'J.K. Rowling', '439554896', 'eng', '2003.11.01', 'Scholastic', 10, 5000),
(4, 'Harry Potter and the Prisoner of Azkaban (Harry Potter  #3)', 'J.K. Rowling/Mary GrandPré', '043965548X', 'eng', '2004.05.01', 'Scholastic Inc.', 17, 5000),
(5, 'Harry Potter Boxed Set  Books 1-5 (Harry Potter  #1-5)', 'J.K. Rowling/Mary GrandPré', '439682584', 'eng', '2004.09.13', 'Scholastic', 21, 5000);

insert into Customers (CustomerID, Name, email, PhoneNumber, Address)
values
(1, 'Gombos Tamás', 'gtamas@gmail.com', '+36301234567', '1149 Budapest, Valahol t;r 8.'),
(2, 'Teszt Elek', 'tesztelek@citromail.hu', '+3620472568', '1011 Bp, Sehol utca 10.'),
(3, 'Remek Elek', 'remekelek@freemail.hu', '+36707654321', '9800 Zalaegerszeg, Köztársaság útja 100.'),
(4, 'Ötös Feladat', 'otosfeladat@nagyonjo.hu', '+3680456123', '1000 Adatbázis, Jól Végzett feladat utca 1.'),
(5, 'Öröm Boldogság', 'oromboldogsag@nagyszeru.hu', '+36309876543', '2100 Ünneplés, Koccintás út 10.');

insert into orders (OrderID, CustomerID, OrderDate, Status, TotalPrice)
values
(1, 1, '2024.01.01', true, 15000),
(2, 2, '2024.02.02', true, 5000),
(3, 3, '2024.03.03', true, 10000),
(4, 4, '2024.04.04', true, 15000),
(5, 5, '2024.05.05', true, 10000);

insert into orderdetails (OrderDetailID, OrderID, BookID, Quantity, Price)
values
(1, 1, 1, 1, 5000),
(2, 1, 2, 1, 5000),
(3, 1, 3, 1, 5000),
(4, 2, 4, 1, 5000),
(5, 3, 5, 2, 10000),
(6, 4, 1, 3, 15000),
(7, 5, 1, 1, 5000),
(8, 5, 2, 1, 5000);

insert into Invoices (InvoiceID, OrderID, InvoiceDate, TotalPrice, Paymentstatus)
values
(1, 1, '2024.01.01', 15000, true),
(2, 2, '2024.02.02', 5000, true),
(3, 3, '2024.03.03', 10000, true),
(4, 4, '2024.04.04', 15000, true),
(5, 5, '2024.05.05', 10000, true);