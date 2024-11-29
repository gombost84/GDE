create table if not exists Books (
	BookID serial not null primary key,
	Title text not null,
	Authors text not null,
	ISBN varchar(13) not null,
	LangCode varchar(3),
	PubDate date,
	Publisher text,
	StockQuantity integer,
	Price money not null
);

create table if not exists OrderDetails (
	OrderDetailID serial not null primary key,
	OrderID integer,
	BookID integer,
	Quantity integer not null,
	Price money
);

create table if not exists Orders (
	OrderID serial not null primary key,
	CustomerID integer,
	OrderDate date not null,
	Status bool,
	TotalPrice money
);

create table if not exists Invoices (
	InvoiceID serial not null primary key,
	OrderID integer,
	InvoiceDate date not null,
	TotalPrice money,
	PaymentStatus bool
);

create table if not exists Customers (
	CustomerID serial not null primary key,
	Name text not null,
	email varchar(252),
	PhoneNumber varchar(64),
	Address text not null
);

alter table OrderDetails
	add constraint bookid_fk foreign key (BookID) references Books(BookID);

alter table Orders
	add constraint customerid_fk foreign key (CustomerID) references Customers(CustomerID);

alter table OrderDetails
	add constraint orderid_fk foreign key (OrderID) references Orders(OrderID);

alter table Invoices
	add constraint orderid_fk foreign key (OrderID) references Orders(OrderID);