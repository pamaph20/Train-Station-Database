
-- Passenger Queries
-- List of all the availble Trips to passengers
SELECT * from trips where TicketPrice > 0

-- Find what trains are departing from a station going on a given route.
Select trainID, platform, Time 
from station_schedule
    where trainid in 
        (select trainid 
        from train_schedule 
        where tripid ='C145-P28');

-- Find what days and departing times a train is leaving using trip ID 
select Date, DepartingTime, trainid
from Train_Schedule
where TripID ='P28-C145';


-- Find what trains are departing from a station going on a given route.
Select trainID, platform, Time from station_schedule
    where trainid in (select trainid 
                    from train_schedule 
                    where tripid ='C145-P28');

--




-- Staff Queries
-- Implemented Queries
        -- Find what passengers are on a train using day and train
        SELECT pass_id from ticket
        where Date = '12/11/2022' and
        ticketid in (select ticketid from passeger_on_train
                    where trainid = '1234');

        -- Find what train a Passenger is on
        SELECT trainID from passeger_on_train
        where ticketid in (SELECT ticketid
                        from ticket
                        where pass_id = 'jmglov19');
        -- Blacklisted passenger 
        SELECT * from blacklisted_passenger;
--Non Implemented Queries
    -- Find what supply orders are going out on a day
    SELECT supplytype, supplierid, quantity 
    from supply_orders
    where Date = '1/10/2023';

    -- Find what train is bringing an order on a given day
    SELECT trainID, orderid 
    from supplies_on_train
    where orderid in (select orderid 
                    from supply_orders
                    where Date = '1/10/2023');

    -- Look at what trains are at what station, what time, on a given date
    Select trainid, time 
    from station_schedule 
    where Date = '12/11/2022';

    -- Grand master list of a station
    SELECT * 
    from station_schedule 
    where locationid = 'Cour145' and Date = '12/11/2022';

    -- Grand Master list of a train schedule
    Select * 
    from train_schedule 
    where trainid = '1234' and Date = '12/11/2022'




--Mechanic
-- Look at what trains are in a train shed
SELECT trainid
from trains_at_shed
where train_shed_location = 'Syra81';

-- List of all the availble Trips
SELECT * from trips;

-- List of unfinshed mainences orders and where they are as well as a short description
SELECT trains_at_shed.trainid, descrip, train_shed_location 
from trains_at_shed, maintence_orders
    where finished = FALSE 
    and maintence_orders.trainid = trains_at_shed.trainid;


-- Insertions

-- New Passenger
Insert into Passenger values(
    (pass_ID, FirstName, LastName)
);

--Pasenger buys a ticket
Insert into ticket values(
    (ticketID, pass_ID, tripID, SupplierID, Date)
);