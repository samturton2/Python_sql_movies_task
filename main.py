# Import pyodbc to connect with SQL
import pyodbc
# import csv to help read the csv file
import csv

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

    # create a function that loads each row as a list into a python list
    def read_csv(self):
        self.movies_list = []
        with open("imdbtitles.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.movies_list.append(row)
        return self.movies_list

    # Search movies list on title
    def search_title(self, title):
        try:
            for movies in self.movies_list:
                if movies[2] == 'title':
                    return movies
            raise AttributeError('Title not in this movie list')
        except:
            print('Enter a valid Title')

    # create a method that can add movies to the northwind db
    def add_movies(self):
        pass
        #self.cursor.execute("CREATE TABLE)

