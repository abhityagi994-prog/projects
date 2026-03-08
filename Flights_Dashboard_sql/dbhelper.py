import mysql.connector
#CONNECT TO THE DATABASE SERVER

#CREATE A DATABASE
#mycursor.execute('CREATE DATABASE <DATABASE NAME>')
#conn.commit()

class DB:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="flights_db"
            )
            self.mycursor=self.conn.cursor()
            print('Connection Established')
        except:
            print('connectionError')

    def fetch_city(self):
        city=[]
        self.mycursor.execute('''
        SELECT DISTINCT(Source) FROM flights
        UNION
        SELECT DISTINCT(Destination) FROM flights
        ''')

        data=self.mycursor.fetchall()
        #print(data) the result is a tuple.

        for i in data:
            city.append(i[0])
        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute(f'''
        SELECT Airline, Route, Dep_Time, Duration, Price FROM flights
        WHERE Source='{source}' AND Destination ='{destination}'
        ''')
        data=self.mycursor.fetchall()
        return data

    def fetch_airlines(self):
        airlines=[]
        frequency=[]
        self.mycursor.execute('''
        SELECT Airline, COUNT(*) FROM flights
        GROUP BY Airline
        ''')
        data=self.mycursor.fetchall()
        for i in data:
            airlines.append(i[0])
            frequency.append(i[1])
        return airlines, frequency

    def busy_airport(self):
        city=[]
        frequency=[]
        self.mycursor.execute('''
        SELECT Source, COUNT(*) FROM (SELECT Source FROM flights
        UNION ALL
        SELECT Destination FROM flights) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        ''')
        data = self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
            frequency.append(i[1])
        return city, frequency

    def daily_frequency(self):
        data=[]
        frequency=[]
        self.mycursor.execute('''
        SELECT Date_of_Journey, COUNT(*) FROM flights
        GROUP BY Date_of_Journey;
        ''')
        result=self.mycursor.fetchall()
        for i in result:
            data.append(i[0])
            frequency.append(i[1])

        return data,frequency