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
    def search_title(self):
        title = input("What movie do you want? : ")
        try:
            for movies in self.movies_list:
                if movies[2] == title:
                    return movies
            raise AttributeError('Title not in this movie list')
        except:
            print('Enter a valid Title')

    # create a method that can creates the movie table in the nw database
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE Movies ({self.movies_list[0][0]} VARCHAR(255)")
        for heading in self.movies_list[0][1:]:
            self.cursor.execute(f"ALTER TABLE Movies ADD {heading} VARCHAR(255)")

    # create a method that can add movies as many movies to the database as user wants
    def add_movies(self):
        while True:
            row = self.search_title()
            # for each column in the row add to the Movies table
            for num in range(len(self.movies_list[0])):
                self.cursor.execute(f"""
                    INSERT INTO Movies ({self.movies_list[num]})
                    VALUES ('{row[num]}');
                    """)
            check = input("add another movie ot Movies? ")
            if check[0].lower() = 'n':
                break




movies_list = []
with open("imdbtitles.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        movies_list.append(row)
print(movies_list)
