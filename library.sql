DROP DATABASE IF EXISTS Library;
create database Library;
use Library;

DROP TABLE IF EXISTS Reader;
create table Reader(
    ReaderID int,
    ReaderName varchar(10) Not NULL,
    Sex varchar(5),
    Age int default 18,
    TEL varchar(12) default NULL,
    primary key (ReaderID),
    unique (ReaderID),
    CHECK ( Sex='man' or Sex='women')
);
DROP TABLE IF EXISTS Book;
create table Book(
  ISBN varchar(20),
  BookName varchar(20) not null ,
  Author varchar(20) default 'anonymous',
  Price int,
    primary key (ISBN),
    unique (ISBN),
    check ( Price>0 )
);
DROP TABLE IF EXISTS CollectionOfBook;
create table CollectionOfBook(
    ISBN varchar(20),
    TotalNum int default 0,
    foreign key (ISBN)
        references Book(ISBN)
);

alter table collectionofbook add constraint check(TotalNum>=0);

DROP TABLE IF EXISTS Borrow;
create table Borrow(
    borrowID int primary key auto_increment,
    BorrowTime DATE ,
    ReaderID int,
    ISBN varchar(20),
    foreign key (ReaderID)
                   references Reader(ReaderID),
    foreign key (ISBN)
                   references collectionofbook(ISBN)
);
DROP TABLE IF EXISTS Sell;
create table Sell(
    sell_id int auto_increment primary key ,
    ISBN varchar(20),
    AlreadySold int,
    price int check ( price>=0 ),
    FOREIGN KEY (ISBN)
                 references Book(ISBN)
                 );

DROP TABLE IF EXISTS PurchaseBook;
create table PurchaseBook(
    PurchaseID int primary key auto_increment,
    ISBN varchar(20) ,
    Price int,
    PurchaseNum int,
    foreign key (ISBN)
        references Book(ISBN)
);
DROP TABLE IF EXISTS Employee;
CREATE table Employee(
    EmployeeID int primary key ,
    EmployName varchar(20),
    EmploySex varchar(5),
    EmployAge int,
    EmployTEL varchar(20),
    Salary int,
    check ( EmploySex ='man' or EmploySex = 'women')
);
DROP TABLE IF EXISTS ReturnOfBook;
create table ReturnOfBook(
    returnID int primary key auto_increment,
    ReturnTime DATE,
    ReaderID int,
    ISBN varchar(20),
    foreign key (ReaderID)
                   references Reader(ReaderID),
    foreign key (ISBN)
                   references collectionofbook(ISBN)
);

insert into reader(readerid, readername, sex, age, tel) values (
                           1,'zyh','man',20,'19825300946'
                          );

insert into book(ISBN, BookName, Author, Price) values (
                  '151515-4654-545','database','',50
                                                       );
insert into collectionofbook(ISBN, Totalnum) values (
                                        '151515-4654-545', 9
                                                    );

create trigger increaseNumberOfBooks after insert on purchasebook
    for each row
    begin
        if not exists(select 1 from collectionofbook where NEW.ISBN in (select ISBN from collectionofbook)) then
            begin
       insert into CollectionOfBook(ISBN, TotalNum) VALUE (NEW.ISBN,NEW.PurchaseNum);
            end;
        else
            begin
                update CollectionOfBook set TotalNum = TotalNum + NEW.PurchaseNum
        where CollectionOfBook.ISBN = NEW.ISBN;
                end;
        end if;
    end;
select version();


create trigger decreaseNumberOfBooks after insert on sell
    for each row
    begin
        update CollectionOfBook set TotalNum = TotalNum-NEW.AlreadySold
        where  CollectionOfBook.ISBN = NEW.ISBN;
    end;

create  trigger borrowBook before insert on borrow
    for each row
    begin
        if (select TotalNum from collectionofbook where CollectionOfBook.ISBN
            = NEW.ISBN
            ) -1 >=0 then
        update collectionofbook set TotalNum = TotalNum-1 where CollectionOfBook.ISBN
        = NEW.ISBN;
        end if;
    end;

insert into borrow(borrowtime, readerid, isbn) VALUES ('2021-3-23','1','1');


create  trigger ReturnBook before insert on returnofbook
    for each row
    begin
        update collectionofbook set TotalNum = TotalNum+1 where CollectionOfBook.ISBN
        = NEW.ISBN;
    end;

insert into returnofbook(returntime, readerid, isbn) values ('2021-3-23','1','1');