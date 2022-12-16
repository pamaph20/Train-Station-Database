
-- Entity relationships
drop table if EXISTS Supplies_On_Train;
drop table if EXISTS Tools_at_Shed;
drop table if EXISTS Ticket_Cancelations;
drop table if EXISTS Passeger_On_Train;
drop table if EXISTS Staff_On_Train;
drop table if EXISTS train_schedule;
drop table if EXISTS Station_Schedule;
drop table if EXISTS Ticket;
drop table if EXISTS Maintence_Orders;
drop table if EXISTS Supply_Orders;
drop table if EXISTS blacklisted_passenger;
drop table if EXISTS trips;
drop table if EXISTS Trains_At_Shed;

-- Base Level Tables
drop table if EXISTS Train_Shed;
drop table if EXISTS Stations;
drop table if EXISTS Train;
drop table if EXISTS Passenger;
drop table if EXISTS staff;
drop table if EXISTS Ticket_Supplier;
drop table if EXISTS AvalibleTools;
drop table if EXISTS Supplies;
drop table if EXISTS supplier;
drop table if EXISTS Locations;


CREATE TABLE Locations(
    LocationID Varchar(10) NOT NULL,
    typeOfLoc Varchar(15),
    PRIMARY KEY (LocationID)
    );

CREATE TABLE Stations (
  LocationID Varchar(10) NOT NULL,
  num_Platfoms int,
  Location Text,
  PRIMARY KEY (LocationID),
  foreign key (LocationID) references Locations(LocationID)

);

CREATE TABLE Train(
  TrainID Varchar(8) NOT NULL,
  Model Varchar(20),
  Year int,
  Color Varchar(20),
  Capacity int,
  PRIMARY KEY (TrainID)
);

CREATE TABLE Passenger (
  pass_ID Varchar(8) NOT NULL,
  FirstName Text,
  LastName Text,
  PRIMARY KEY (pass_ID)
);

CREATE TABLE Blacklisted_Passenger (
  pass_ID Varchar(8),
  Reason Text,
  PRIMARY KEY (pass_ID),
  foreign key (pass_ID) references Passenger(pass_ID)
);


CREATE TABLE Staff (
  StaffID Varchar(8) NOT NULL,
  FirstName Text,
  LastName Text,
  Age Int,
  job Varchar(15),
  PRIMARY KEY (StaffID)
);

CREATE TABLE supplier (
  SupplierID VarChar(8),
  LocatonID Varchar(8),
  TypeOfStuff Text,
  Name Text,
  PRIMARY KEY (SupplierID)
);

CREATE TABLE AvalibleTools (
  ToolID Varchar(4),
  Tool_description text,
  PRIMARY KEY (ToolID)
);

CREATE TABLE Train_Shed (
  LocationID Varchar(8),
  Capacity int,
  PRIMARY KEY (LocationID),
  foreign key (LocationID) references Locations(LocationID)
);

CREATE table Tools_at_Shed (
  LocationID VarChar(8),
  ToolID VarChar(4),
  PRIMARY key (LocationID),
  Foreign key (LocationID) references Train_Shed(LocationID),
  Foreign key (ToolID) references AvalibleTools(ToolID)
);


CREATE TABLE Trips (
  TripID Varchar(8),
  FromLocationID Varchar(8),
  ToLocationID Varchar(8),
  TicketPrice double precision,
  PRIMARY KEY (TripID),
  foreign key (FromLocationID) references Locations(LocationID),
  foreign key (TOLocationID) references Locations(LocationID)


);

CREATE TABLE Ticket_Supplier (
  CompanyID Varchar(8),
  CompanyName text,
  PRIMARY KEY (CompanyID)
);

CREATE TABLE Ticket (
  TicketID VarChar(8),
  pass_ID Varchar(8),
  TripID Varchar(8),
  CompanyID Varchar(8),
  Date Date,
  PRIMARY KEY (TicketID),
  foreign key (pass_ID) references Passenger(pass_ID),
  foreign KEY (TripID)  references Trips(TripID),
  Foreign key (CompanyID) references Ticket_Supplier(CompanyID)
);

CREATE TABLE Ticket_Cancelations (
  CanceledTicketID VarChar(8),
  PRIMARY KEY (CanceledTicketID),
  foreign key (CanceledTicketID) references Ticket(TicketID)

);

CREATE TABLE Train_Schedule (
  TrainID Varchar(8),
  Date Date,
  TripID Varchar(8),
  DepartingTime Time,
  EndingTime Time,
  PRIMARY KEY (TrainID, Date, TripID),
  foreign key (TrainId) references Train(TrainID),
  foreign key (TripID) references Trips(TripID)

);


CREATE TABLE Passeger_On_Train (
  TrainID Varchar(8),
  TicketID VarChar(8),
  PRIMARY KEY (TrainID, TicketID),
  foreign key (TrainID) references Train(TrainID),
  foreign key (TicketID) references Ticket(TicketID)
);


CREATE TABLE Staff_On_Train (
  TrainId Varchar(8),
  TripID Varchar(8),
  StaffID Varchar(8),
  Date Date,
  PRIMARY KEY (TrainId, TripID, Date),
  foreign key (TrainID) references Train(TrainID),
  foreign key (TripID) references Trips(TripID),
  foreign key (StaffID) references Staff(StaffID)

);

CREATE TABLE Station_Schedule (
  LocationID varchar(8),
  Date Date,
  Time Time,
  Platform Int,
  TrainID Varchar(8),
  PRIMARY KEY (LocationID, Date),
  foreign key (LocationID) references Stations(LocationID)
);



CREATE TABLE Maintence_Orders (
  MaintOrderID Varchar(8),
  DateFilled Date,
  Finished Boolean,
  TrainID Varchar(8),
  Descrip text,
  PRIMARY KEY (MaintOrderID),
  foreign key (TrainID) references Train(TrainID)
);


CREATE TABLE Supplies (
  ItemID Varchar(8),
  nameOfSupplies text,
  PRIMARY KEY (ItemID)
);


CREATE TABLE Supply_Orders (
  OrderID Varchar(8),
  SupplyType Varchar(8),
  SupplierID VarChar(8),
  Quantity int,
  Date Date,
  PRIMARY KEY (OrderID),
  foreign key (SupplyType) references Supplies(ItemID),
  foreign key (SupplierID) references supplier(SupplierID)
);


CREATE TABLE Supplies_On_Train (
  OrderID VarChar(8),
  TrainID Varchar(8),
  PRIMARY KEY (OrderID, TrainID),
  foreign key (OrderID) references Supply_Orders(OrderID),
  foreign key (TrainID) references Train(TrainID)
);

CREATE TABLE Trains_At_Shed (
  Train_Shed_Location VarChar(8),
  TrainID VarChar(8),
  PRIMARY key(Train_Shed_Location),
  foreign key(Train_Shed_Location) references Train_Shed(LocationID),
  foreign key (TrainID) references Train(TrainID)
);