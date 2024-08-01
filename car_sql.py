# import sys
# print(sys.path)
# import sys
# sys.path.append('D:\anaconda3\Lib\site-packages\cx_Oracle')
import cx_Oracle
def connect_to_oracle():
    # Connect to your Oracle Database
    cx_Oracle.init_oracle_client(lib_dir= r"D:\DB\dbhomeXE\bin")
    connection = cx_Oracle.connect("system", "keer")
    return connection
connection = connect_to_oracle()
# def login():
#     connection = connect_to_oracle()
#     cursor = connection.cursor()

#     # Check user credentials in the database
#     query = "SELECT * FROM test"
#     cursor.execute(query)
#     user = cursor.fetchone()
#     print(user)

#     cursor.close()
#     connection.close()
#     return user
# login()

def vehicle_id():
    cursor = connection.cursor()
    q='select * from vehicles'
    cursor.execute(q)
    record=cursor.fetchall()
    r=record[-1][0]
    s=r[1::]
    num=int(s)+1
    x='v'+str(num)
    vid=x
    cursor.close()
    return vid

def add_vehicle(vid,model,make,year,rentalrate,seat,Ac):
    cursor = connection.cursor()
    q=f"INSERT INTO Vehicles (VehicleID, Model, Make, Year, RentalRate,Seat,Ac) VALUES ('{vid}','{model}','{make}',{year},{rentalrate},{seat},'{Ac}')"
    print(q)
    cursor.execute(q)
    cursor.execute('commit')
    print('successfully added')
    cursor.close()

def delete_vehicle(vid):
    cursor = connection.cursor()
    q=f"delete from vehicles where vehicleid='{vid}'"
    print(q)
    cursor.execute(q)
    cursor.execute('commit')
    cursor.close()

def update_vehicle(vid,rentalrate):
    cursor = connection.cursor()
    q=f"update vehicles set rentalrate={rentalrate} where vehicleid='{vid}'"
    print(q)
    cursor.execute(q)
    cursor.execute('commit')
    cursor.close()

def display_vehicle():
    cursor = connection.cursor()
    q='select * from vehicles'
    cursor.execute(q)
    record=cursor.fetchall()
    
    cursor.execute('commit')
    cursor.close()
    return record

#display_vehicle()
#update_vehicle('v10',1000)
#delete_vehicle('v11')
#add_vehicle('v11', 'Explorer', 'Renault', 2020, 500)
# def display_cust_given(fname,lname):
#     cursor=connection.cursor()
#     q='select * from customers'
#     record=cursor.fetchall()
#     record=cursor.fetchall()
#     for i in record:
#         if i[1].lower()==fname.lower() and i[2].lower()==lname:
#             cid=i[0]
#             cursor.close()
#             return i
   

    
def identify_cust(fname,lname):
    cursor=connection.cursor()
    q='select * from customers'
    cursor.execute(q)
    record=cursor.fetchall()
    for i in record:
        if i[1].lower()==fname.lower() and i[2].lower()==lname:
            cid=i[0]
            cursor.close()
            return cid
    cursor.close()
    return None

#print(identify_cust('jane','smith'))

def cust_id():
    cursor = connection.cursor()
    q='select * from customers'
    cursor.execute(q)
    record=cursor.fetchall()
    r=record[-1][0]
    s=r[1::]
    num=int(s)+1
    x='c'+str(num)
    cid=x
    cursor.close()
    return cid

    

def add_customer(cid,fname,lastname,email,phone,address):
    cursor = connection.cursor()
    q=f"INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address) VALUES ('{cid}', '{fname}', '{lastname}', '{email}', '{phone}', '{address}')"
    cursor.execute(q)
    cursor.execute('commit')
    cursor.close()


def delete_customer(cid):
    cursor = connection.cursor()
    q=f"delete from customers where customerid='{cid}'"
    print(q)
    cursor.execute(q)
    cursor.execute('commit')
    cursor.close()

def display_customer():

    cursor = connection.cursor()
    q='select * from customers'
    cursor.execute(q)
    record=cursor.fetchall()
    cursor.execute('commit')
    cursor.close()
    return record

# cid=cust_id()
# print(cid)
# add_customer( cid,'keer', 'Don', 'keer.doe@example.com', '8828410316', 'anna nagar')
# delete_customer('c10')
#print(display_customer())
def rental_id():
    cursor = connection.cursor()


    q='select * from rentals'
    cursor.execute(q)
    record=cursor.fetchall()
    r=record[-1][0]
    s=r[1::]
    num=int(s)+1
    x='r'+str(num)
    rid=x
    cursor.close()
    return rid

def add_rental(RentalID, CustomerID, VehicleID, RentalDate, ReturnDate):
    cursor = connection.cursor()
    print(RentalDate,ReturnDate)
    q=f"INSERT INTO rentals (RentalID, CustomerID, VehicleID, RentalDate, ReturnDate) VALUES ('{RentalID}', '{CustomerID}', '{VehicleID}', TO_DATE('{RentalDate}', 'YYYY-MM-DD'), TO_DATE('{ReturnDate}', 'YYYY-MM-DD'))"
    print(q)
    cursor.execute(q)
    r=f"UPDATE Rentals SET TotalCost = (RETURNDATE - RENTALDATE) * (SELECT RentalRate FROM Vehicles WHERE VehicleID = '{VehicleID}') WHERE RentalID = '{RentalID}'"
    cursor.execute(r)
    cursor.execute('commit')
    cursor.close()


def front_rental(cid,vid,RentalDate, ReturnDate):
    cursor=connection.cursor()
    rid=rental_id()
    q=f"INSERT INTO rentals (RentalID, CustomerID, VehicleID, RentalDate, ReturnDate) VALUES ('{rid}', '{cid}', '{vid}', '{RentalDate}', '{ReturnDate}')"
    print(q)
    cursor.execute(q)
    r=f"UPDATE Rentals SET TotalCost = (RETURNDATE - RENTALDATE) * (SELECT RentalRate FROM Vehicles WHERE VehicleID = '{vid}') WHERE RentalID = '{rid}'"
    cursor.execute(r)
    cursor.execute('commit')
    cursor.close()


def delete_rental(rid):
    cursor = connection.cursor()
    q=f"delete from rentals where rentalid='{rid}'"
    print(q)
    cursor.execute(q)
    cursor.execute('commit')
    cursor.close()



def display_rental():
    cursor = connection.cursor()
    q='select * from rentals'
    cursor.execute(q)
    record=cursor.fetchall()
    cursor.execute('commit')
    cursor.close()
    return record


#delete_rental('r9')
# rid=rental_id()
# add_rental(rid)
#print(display_rental())

def display_rental_history():
    cursor = connection.cursor()
    q='select * from deleted_rental'
    cursor.execute(q)
    record=cursor.fetchall()
    cursor.execute('commit')
    cursor.close()
    return record
#print(display_rental_history())



def bill(cid,vid,rid):
    cursor = connection.cursor()
    s=f"""DECLARE
        result_cursor SYS_REFCURSOR;
        fname VARCHAR2(50);
        lname VARCHAR2(50);
        start_date DATE;
        return_date DATE;
        unit_price NUMBER;
        total_cost NUMBER;
    BEGIN
        result_cursor := GetRentalInfoList('{cid}','{vid}','{rid}');

        LOOP
            FETCH result_cursor INTO fname,lname,start_date, return_date, unit_price, total_cost;
            EXIT WHEN result_cursor%NOTFOUND;
            delete from bill;
            insert into bill values(fname,lname,start_date,return_date,unit_price,total_cost);
        END LOOP;

        CLOSE result_cursor;
    END;
    """
    cursor.execute(s)
    q='select * from bill'
    cursor.execute(q)
    record=cursor.fetchone()
    cursor.execute('commit')
    cursor.close()
    return record

#print(bill('c11','v3','r11'))

# def add_agent():
#     cursor=connection.cursor()
#     q='select * from agent'
#     cursor.execute(q)
#     record=cursor.fetchall()
#     cursor.execute('commit')
#     cursor.close()
#     return record


# def del_agent(aid):
#     cursor=connection.cursor()
#     q1=f"delete from agent where agentid='{aid}'"
#     q2=f"delete from vehicles where agentid='{aid}'"
#     cursor.execute(q1)
#     cursor.execute(q2)
#     cursor.execute('commit')
#     cursor.close()
      
def display_bill():
    cursor = connection.cursor()
    
    q='select * from bill'
    cursor.execute(q)
    record=cursor.fetchone()
    cursor.execute('commit')
    cursor.close()
    return record
#print(display_bill())

