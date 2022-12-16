import psycopg2
import json
from tabulate import tabulate
#these are for the randomly constructed id's
import string
import random
id_len = 8
#Connect to our document databse
filename = 'Train_Boys.json'
database = json.load(open('Train_Boys.json'))
location = "Please select station desired \n 1) Grand Central Station \n 2) Chicago Union Station \n 3) Washington Union Station \n 4) Pennsylvania Station \n 5) Go back \n"
pass_options = "Please select one of the 3 options: \n 1) Find what trains are departing from a station going on a given route. \n 2) Purchase Tickets \n 3) Find what days and departing times a train is leaving using trip ID \n 4) Go Back \n"
staff_options = "Please Select one of the 3 options: \n 1) Locate passengers train \n 2) Show Trains \n 3) Display Blacklisted Passengers list \n 4) Go Back \n"
mechanic_options = "Please Select one of the 3 options: \n 1) Display Train Shed \n 2) Display all unfinished maintenance Orders \n 3) Display all trips  \n 4) Go Back \n"

#CRUD
def create_passenger(new_user):
    """
    Writes to the document database after creating a new passenger
    :param group:
    :param id:
    :param password:
    :return:
    """
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data['users']['Passenger'].update(new_user)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
    file.close()


def check_login(id,password,group):
    """
    Takes in
    :param id:
    :param password:
    :param group:
    :return: True or false if the login is correct
    """

    if group == 'Passenger':
        if database['users'][group][id]['password'] == password:
            return True
    else:
        if database['users'][group][id] == password:
            return True
    return False
def connect_ratings():
    """
    Connect to the ratings database and return the connection object
    Function exits the program if there is an error
    :return: connection object
    """
    try:
        conn = psycopg2.connect(
            dbname="Train_Boys",
            user="pamaph20",
            password='Harabec11!',
            host="ada.hpc.stlawu.edu"

        )
    except psycopg2.Error:
        print("Error: cannot connect to database")
        exit()
    finally:
        return conn

def MainMenu():
    """
    Present the user with a menu and return selection
    only if valid
    :return: option selected
    """
    while True:
        print("1) Login as passenger")
        print("2) Login as staff")
        print("3) Login as mechanic")
        print("Q) Quit")
        opt = input("> ")
        if opt in ['1', '2','3', 'q', 'Q']:
            break
    return opt
def PassengerLogin(conn):
    """
    present the user with a passenger login menu
    :param conn:
    :return:
    """
    UserType = input("Please specify one of two options: \n 1) New User \n 2) Existing User \n 3) Go Back \n")
    #check to make sure that the user id is not avaliable??
    if UserType == '3':
        MainMenu()
    if UserType == '1':
        #generates a new passenger id of length 8
        new_pass_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=id_len))
        pass_password = input("Please enter new password for: " + new_pass_id +"\n")
        first_name = input("Please Enter First Name: ")
        last_name = input("Please Enter Last Name: ")
        insert_user(new_pass_id, first_name, last_name, conn)
        new_passenger = {str(new_pass_id): {'password': pass_password, 'fist_name': first_name, 'last_name': last_name}}
        create_passenger(new_passenger)
        pass_menu(new_pass_id, conn)
    if UserType == '2':
        old_pass_id = input("Please Enter passenger Id: ")
        if old_pass_id not in database['users']['Passenger']:
            print("Passenger Id: " + old_pass_id + " does not exist")
            return PassengerLogin(conn)
        else:
            pass_word = input("Please enter " + old_pass_id + "'s password: \n")
            if not check_login(old_pass_id, pass_word, 'Passenger'):
                print("Invalid password:" + pass_word + " for passenger " + old_pass_id)
                return PassengerLogin(conn)
            else:
                pass_menu(old_pass_id, conn)


def insert_user(pass_id, FirstName, LastName, conn):
    """
    Insert  A new user into the sql database
    :param pass_id:
    :param FirstName:
    :param LastName:
    :param conn:
    :return:
    """
    curr = conn.cursor()
    cmd = """
    Insert into passenger values(%s,%s,%s);
    """
    curr.execute(cmd, (pass_id,FirstName,LastName,))
    conn.commit()


def pass_menu(x, conn):
    """
    Menu with all avaliable options for any passenger that is currently logged in
    :param pass_id:
    :return:
    """
    print("Connected User: " + x)
    option = (input(location))
    if option == '5':
        PassengerLogin(conn)
    if option == '1':
        station = 'Grand_Central'
        selection = (input(pass_options))
        if selection == '4':
            pass_menu(x, conn)
        if selection == '1':
            display_station_schedual(x,station, conn)
        if selection == '2':
            purchase_tickets(station,conn,x)
        if selection == '3':
            search_Trips(x,station,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return pass_menu(x, conn)
    if option == '2':
        station = "Chicago_Union"
        selection = (input(pass_options))
        if selection == '4':
            pass_menu(x, conn)
        if selection == '1':
            display_station_schedual(x,station, conn)
        if selection == '2':
            purchase_tickets(station,conn,x)
        if selection == '3':
            search_Trips(x,station,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return pass_menu(x, conn)
    if option == '3':
        station = 'Washingtion_Union'
        selection = (input(pass_options))
        if selection == '4':
            pass_menu(x, conn)
        if selection == '1':
            display_station_schedual(x,station, conn)
        if selection == '2':
            purchase_tickets(station,conn,x)
        if selection == '3':
            search_Trips(x,station,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return pass_menu(x, conn)
    if option == '4':
        station = 'Pennsylvania_Station'
        selection = (input(pass_options))
        if selection == '4':
            pass_menu(x, conn)
        if selection == '1':
            display_station_schedual(x,station, conn)
        if selection == '2':
            purchase_tickets(station, conn,x)
        if selection == '3':
            search_Trips(x,station,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return pass_menu(x, conn)
    else:
        print("Invalid station selected: " + option + " please try again.")
        return pass_menu(x, conn)
def display_station_schedual(x,station, conn):
    """
    For Passenger use only
    :param station:
    :param conn:
    :return: Information list about specfic station location
    """
    print("Selected Station: " + station + "\n")
    tripid = input("Please input trip id: \n")
    # Ticket Query Goes here
    cmd = """
        Select 
            trainID, platform, Time 
        from 
            station_schedule
        where 
            trainid in 
                (select 
                    trainid 
                 from 
                    train_schedule 
                 where 
                    (tripid) = %s);
        """
    cur = conn.cursor()
    cur.execute(cmd, (tripid,))
    table = [("Train Id", "Platform", "Time")]
    for row in cur:
        table.append(row[0:3])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to passenger menu \n 2) Quit \n")
    if i == '1':
        pass_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        pass_menu(x, conn)


def purchase_tickets(station, conn, x):
    """
    For passenger use only
    :param station:
    :param conn:
    :return: Purchased ticket information
    """
    print("Selected Station: " + station + "\n")
    pass_ID = x
    ticketID = ''.join(random.choices(string.ascii_uppercase + string.digits, k= id_len))
    tripID = input("Please Enter Wanted Trip ID: \n")
    SupplierID = input("Please Enter Supplier ID: \n")
    date = input('Please Enter Date: \n')
    cur = conn.cursor()
    buy = """
    Insert into ticket values(
    %s, %s,  %s,  %s,  %s
    );
    """
    cur.execute(buy, (ticketID, pass_ID, tripID.upper(), SupplierID, date,))
    conn.commit()
    show = """
    select toLocationid, fromLocationid, ticketprice 
    from trips
    where tripid = (select tripid from ticket where ticketid = %s)
    """
    cur.execute(show, (ticketID,))
    table = [("To LocationId", "From LocationId", "Ticket Price")]
    for row in cur:
        table.append(row[0:3])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to passenger menu \n 2) Quit \n")
    if i == '1':
        pass_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        pass_menu(x, conn)



def search_Trips(x,station, conn):
    """
    For Passenger use only
    :param station:
    :param conn:
    :return: Searched trip information
    """
    print("Selected Station: " + station + "\n")
    TripID= (input("Please Enter Trip ID: \n")).upper()
    cmd = """
    select 
        Date, DepartingTime, trainid
    from 
        Train_Schedule
    where 
        (TripID) = %s;
    """
    cur = conn.cursor()
    cur.execute(cmd, (TripID,))
    table = [("Date", "Departing Time", "Train Id")]
    for row in cur:
        table.append(row[0:3])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to passenger menu \n 2) Quit \n")
    if i == '1':
        pass_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        pass_menu(x, conn)





def StaffLogin(conn):
    """
    Present the user with the ability to log in as a staff member
    :param conn:
    :return:
    """
    staff_Id = input("Please enter your staff Id: ")
    if staff_Id not in database['users']['Staff']:
        print("Invalid Staff Id: " + staff_Id)
        return StaffLogin(conn)
    else:
        staff_password = input("Please enter staff " + staff_Id + "'s password: \n")
        if not check_login(staff_Id, staff_password, 'Staff'):
            print("Invalid password: " + staff_password + " for staff user: " + staff_Id)
            return(StaffLogin(conn))
        staff_menu(staff_Id, conn)

def staff_menu(x, conn):
    """
    Menu for the staff
    :param x:
    :param conn:
    :return: options
    """
    print("Connected Staff: " + x)
    o = input(location)
    if o == '5':
        return MainMenu()
    if o == '1':
        station = 'Grand_Central'
        selection = (input(staff_options))
        if selection == '4':
            MainMenu()
        if selection == '1':
            find_pass(station, conn, x)
        if selection == '2':
            grand_master_train_info(station, conn, x)
        if selection == '3':
            blacklist_passenger_list(station, conn, x)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return pass_menu(x, conn)
    if o == '2':
        station = "Chicago_Union"
        selection = (input(staff_options))
        if selection == '4':
            staff_menu(x, conn)
        if selection == '1':
            find_pass(station, conn, x)
        if selection == '2':
            grand_master_train_info(station, conn, x)
        if selection == '3':
            blacklist_passenger_list(station, conn, x)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return staff_menu(x, conn)
    if o == '3':
        station = 'Washingtion_Union'
        selection = input(staff_options)
        if selection == '4':
            staff_menu(x, conn)
        if selection == '1':
            find_pass(station, conn, x)
        if selection == '2':
            grand_master_train_info(station, conn, x)
        if selection == '3':
            blacklist_passenger_list(station, conn, x)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return staff_menu(x, conn)
    if o == '4':
        station = 'Pennsylvania_Station'
        selection = (input(staff_options))
        if selection == '4':
            staff_menu(x, conn)
        if selection == '1':
            find_pass(station, conn, x)
        if selection == '2':
            grand_master_train_info(station, conn, x)
        if selection == '3':
            blacklist_passenger_list(station, conn, x)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return staff_menu(x, conn)
    else:
        print("Invalid station selected: " + o + " please try again.")
        return staff_menu(x, conn)


def find_pass(location, conn, x):
    """
    For Use of Staff only
    :param location:
    :param conn:
    :return: Location of a specified passengers train
    """
    print("Connected Staff: " + x + "\n")
    pass_id = input("What is the passengers id: \n")
    if pass_id not in database['users']['Passenger']:
            print("Passenger Id: " + pass_id + " does not exist")
            return find_pass(location, conn, x)
    else:
        cmd = """
        SELECT 
            trainID 
        from 
            passeger_on_train
        where 
            ticketid in (SELECT ticketid
                    from ticket
                    where (pass_id) = %s);
        """
        cur = conn.cursor()
        cur.execute(cmd, (pass_id,))
        table = [("Train Id",)]
        for row in cur:
            table.append(row[0:1])
        print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
        i = input("Please Select one of the two options \n 1) Return Back to staff menu \n 2) Quit \n")
        if i == '1':
            staff_menu(x, conn)
        if i == '2':
            quit(conn)
        else:
            print("Invalid Option selected: " + i)
            staff_menu(x, conn)
def grand_master_train_info(train_id, conn, x):
    """
    For Use of Staff and Mechanics Only
    :param train_id:
    :param conn:
    :return: Generated Information list of everything and everyone that is on a train on a given date
    """
    date = input("Please enter wanted date: \n")
    cmd = """
    Select 
        trainid, time 
    from 
        station_schedule 
    where 
        (Date) = %s;
    """
    cur = conn.cursor()
    cur.execute(cmd, (date,))
    table = [("Train Id","Time",)]
    for row in cur:
        table.append(row[0:2])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to staff menu \n 2) Quit \n")
    if i == '1':
        staff_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        staff_menu(x, conn)
def blacklist_passenger_list(station, conn,x):
    """
    For Staff use only
    :param pass_id:
    :param conn:
    :return: Show blacklisted Passenger list
    """
    print("Passengers blacklisted at " + station + "\n")
    cmd = """
        SELECT * from blacklisted_passenger;
        """
    cur = conn.cursor()
    cur.execute(cmd)
    table = [("Passenger Id", "Reason",)]
    for row in cur:
        table.append(row[0:2])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to staff menu \n 2) Quit \n")
    if i == '1':
        staff_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        staff_menu(x, conn)



def MechanicLogin(conn):
    """
    Return the user with a login menu for the mechanic
    :param conn:
    :return:
    """
    mechanic_id = input("Please enter your mechanic Id: ")
    if mechanic_id not in database['users']['Mechanics']:
        print("Invalid Mechanic Id: " + mechanic_id)
        return StaffLogin(conn)
    else:
        mechanic_pass = input("Please enter mechanic " + mechanic_id + "'s password: \n")
        if not (mechanic_id,mechanic_pass,'Mechanics'):
            print("Invalid password: " + mechanic_pass + " for mechanic user: " + mechanic_id)
            return (MechanicLogin(conn))
        mechanic_menu(mechanic_id, conn)
def mechanic_menu(x, conn):
    """
    Menu for the mechanic
    :param x:
    :param conn:
    :return:
    """
    print("Connected Mechanic: " + x)
    option = input(location)
    if option == '5':
        MainMenu()
    if option == '1':
        station = 'Grand_Central'
        selection = (input(mechanic_options))
        if selection == '4':
            mechanic_menu(x, conn)
        if selection == '1':
            check_shed(x, conn)
        if selection == '2':
            display_maintenance(x,station, conn)
        if selection == '3':
            display_trips(x,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return mechanic_menu(x, conn)
    if option == '2':
        station = "Chicago_Union"
        selection = (input(mechanic_options))
        if selection == '4':
            check_shed(x, conn)
        if selection == '1':
            display_maintenance(x, conn)
        if selection == '2':
            grand_master_train_info(x,station, conn)
        if selection == '3':
            display_trips(x,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return mechanic_menu(x, conn)
    if option == '3':
        station = 'Washingtion_Union'
        selection = (input(mechanic_options))
        if selection == '4':
            mechanic_menu(x, conn)
        if selection == '1':
            check_shed(x, conn)
        if selection == '2':
            display_maintenance(x,station, conn)
        if selection == '3':
            display_trips(x,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return mechanic_menu(x, conn)
    if option == '4':
        station = 'Pennsylvania_Station'
        selection = (input(mechanic_options))
        if selection == '4':
            mechanic_menu(x, conn)
        if selection == '1':
            check_shed(x, conn)
        if selection == '2':
            display_maintenance(x,station, conn)
        if selection == '3':
            display_trips(x,conn)
        else:
            print("Invalid option selected: " + selection + " please try again")
            return mechanic_menu(x, conn)
    else:
        print("Invalid station selected: " + option + " please try again.")
        return mechanic_menu(x, conn)
def check_shed(x, conn):
    """
    For Mechanic Use only
    :param location:
    :param conn:
    :return: All Trains within the train shed
    """

    train_shed_location = input("Please enter train shed ID: \n")
    cmd = """
            SELECT trainid
            from trains_at_shed
            where train_shed_location = %s;
            """
    cur = conn.cursor()
    cur.execute(cmd, (train_shed_location,))
    table = [("Train ID",)]
    for row in cur:
        table.append(row[0:1])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to mechanic menu \n 2) Quit \n")
    if i == '1':
        mechanic_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        mechanic_menu(x, conn)

def display_maintenance(x,station, conn):
    """
    For Mechanic Use Only
    :param :
    :param conn:
    :return: Display all maintenance orders
    """
    print("Maintenance Orders at " + station + "\n")
    cmd = """
            SELECT trains_at_shed.trainid, descrip, train_shed_location 
            from trains_at_shed, maintence_orders
            where finished = FALSE 
            and maintence_orders.trainid = trains_at_shed.trainid;
            """
    cur = conn.cursor()
    cur.execute(cmd)
    table = [("Train ID", "Reason", "Train Shed Location")]
    for row in cur:
        table.append(row[0:3])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to mechanic menu \n 2) Quit \n")
    if i == '1':
        mechanic_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        mechanic_menu(x, conn)

def display_trips(x,conn):
    """
    For Mechanic Use Only
    :param conn:
    :return: List of all avaliable trips
    """
    cmd = """SELECT * from trips;"""
    cur = conn.cursor()
    cur.execute(cmd)
    table = [("Trip ID")]
    for row in cur:
        table.append(row[0:1])
    print(tabulate(table, tablefmt='fancy_grid', headers="firstrow") + "\n \n \n")
    i = input("Please Select one of the two options \n 1) Return Back to mechanic menu \n 2) Quit \n")
    if i == '1':
        mechanic_menu(x, conn)
    if i == '2':
        quit(conn)
    else:
        print("Invalid Option selected: " + i)
        mechanic_menu(x, conn)


def quit(conn):
    print("Thank you for using TrainBoys by TrainBy.CO")
    exit()

if __name__ == '__main__':
    conn = connect_ratings()
    opt_map = {
               '1': PassengerLogin,
               '2': StaffLogin,
               '3': MechanicLogin,
               'Q': quit,
               'q': quit
               }
    while True:
        opt = MainMenu()
        opt_map[opt](conn)

