# Import pyodbc to connect with SQL
import pyodbc
# # Import pandas library to interact with the csv file
# import pandas

#create class that can export data from csv file
class MoviesDatabase:
    # get a connection to the northwind database
    def __init__(self, username, password):
        self.username = username
        self.password = password
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        self.northwind_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        # create a class variable that's the cursor
        self.cursor = self.northwind_connection.cursor()

    # def import_data(self):
    #     data = pandas.read_csv(r'/imdbtitles.csv')
    #     self.dataframe = pandas.DataFrame(data, columns = ['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres'])

    # Create a function that reads each line of the csv file, loading it into a dictionary
    def read_csv_lines(self):
        with open("imdbtitles.csv", 'r') as movies_db:
           for line in movies_db:
                print(line)