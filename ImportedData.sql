INSERT INTO Locations values
    ('Cour145', 'Station'),
    ('Platt28', 'Station'),
    ('Targ250', 'Supplier'),
    ('Syra81', 'Shed'),
    ('Cant26', 'Shed'),
    ('GraCen1', 'Station'),
    ('ChicUni', 'Station'),
    ('WashU', 'Station'),
    ('PennSt','Station');

Insert into Train values
    ('1234', 'Diesal Engine', 1998, 'Brown', 200),
    ('5678', 'Diesal Engine', 2001, 'Black', 150),
    ('2828', 'Steam Locomotive', 1987, 'Black-Red', 100),
    ('1729', 'Diesel Locomotive', 1989, 'Gold', 400),
    ('5612','Steam Locomotive', 1812, 'Black-White', 150);

Insert into Stations values
    ('Cour145', 18, 'Coursant South'),
    ('Platt28', 4, 'Plattsburgh New York'),
    ('GraCen1', 16, 'Grand Central Station'),
    ('ChicUni', 19, 'Chicago Union'),
    ('WashU', 17, 'Washington Union'),
    ('PennSt', 6, 'Penn Station');

Insert into Passenger values
    ('jmglov19', 'John', 'Glover'),
    ('pamaph20', 'Drew', 'Maphey'),
    ('robert20', 'Rob', 'Fusting'),
    ('25r9wmlf', 'Drew', 'Maphey');

Insert into Blacklisted_Passenger values
    ('robert20', 'NOT a nice Guy');

Insert into Staff values
    ('Ehar200', 'Ed', 'Harcourt', 65, 'Conductor'),
    ('Lisa200', 'Lisa', 'Torey', 42, 'Mechanic');

Insert into supplier values
    ('Targ250', 'Platts12', 'Department Goods', 'Target-Plattsburgh');

Insert into AvalibleTools values
    ('Dr45', 'Drill 45 Nut'),
    ('Ph12', 'Phillups head screwdriver');

Insert into Train_Shed values
    ('Syra81', 20),
    ('Cant26', 4);

Insert into Tools_at_Shed values
    ('Syra81', 'Dr45');

Insert into Trips values
    ('C145-P28', 'Cour145', 'Platt28', 14.25),
    ('P28-C145', 'Platt28', 'Cour145', 15.00),
    ('T250-S81', 'Targ250', 'Syra81', 0.00),
    ('Gr1-ChiU', 'GraCen1', 'ChicUni', 60.00),
    ('WaU-ChiU', 'WashU', 'ChicUni', 28.95),
    ('Gr1-PenS', 'GraCen1', 'PennSt', 30.25),
    ('PenS-P28', 'PennSt', 'Platt28', 17.00);

Insert into Ticket_Supplier values
    ('SeatGeek', 'SeatGeek Train Tickets');

Insert into Ticket values
    ('00000001', 'jmglov19', 'P28-C145', 'SeatGeek', '12/11/2022'),
    ('00000002', 'pamaph20', 'P28-C145', 'SeatGeek', '12/11/2022'),
    ('00000003', '25r9wmlf', 'Gr1-ChiU', 'SeatGeek', '12/26/2022');

Insert into Train_Schedule values
    ('1234', '12/11/2022', 'P28-C145', '12:45', '17:23'),
    ('1234', '12/11/2022', 'C145-P28', '17:23', '21:47'),
    ('5678', '12/13/2022', 'Gr1-ChiU', '7:23', '14:18'),
    ('1234', '12/13/2022', 'WaU-ChiU', '14:23', '16:47'),
    ('5612', '12/13/2022', 'PenS-P28', '12:23', '21:47'),
    ('1234', '12/14/2022', 'C145-P28', '17:23', '21:47'),
    
    ('5678', '12/15/2022', 'T250-S81', '4:23', '16:47'),
    ('5612', '12/26/2022', 'Gr1-ChiU', '7:23', '8:47'),
    ('1234', '12/27/2022', 'C145-P28', '17:23', '21:47');



Insert into Passeger_On_Train values
    ('1234', '00000001'),
    ('1234', '00000002');

Insert into Staff_On_Train values
    ('1234', 'P28-C145', 'Ehar200', '12/11/2022');

Insert into Station_Schedule values
    ('Cour145', '12/11/2022', '17:23', 3, '1234');

Insert into Supplies values
    ('Lumber44', 'lumber boards 4x4');

Insert into Supply_Orders values
    ('TargLum1', 'Lumber44', 'Targ250', 200, '1/10/2023'),
    ('TargLum2', 'Lumber44', 'Targ250', 200, '1/15/2022');

Insert into Supplies_On_Train values
    ('TargLum1', '5678'),
    ('TargLum2', '5678');

Insert into Trains_At_Shed values
    ('Syra81', '2828'),
    ('Cant26', '1729');
    
    

Insert into Maintence_Orders values
    ('xba1', '12/1/2021', False, '2828', 'New Smoke stack'),
    ('rit', '10/15/2021', False, '1729', 'New Fuel Intake');

