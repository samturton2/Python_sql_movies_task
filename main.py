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
        # get rid of first 3 letters in movies titleType heading name manually
        self.movies_list[0][0] = self.movies_list[0][0][3:]
        # declare column titles as a string for queries
        self.columns = ", ".join(str(word) for word in self.movies_list[0])
        return self.movies_list

    # Search movies list on title, bare in mind read_cvs module has to be called first
    def search_title(self):
        title = input("What movie do you want? : ")
        try:
            for movies in self.movies_list:
                if movies[2].lower() == title.lower().strip():
                    return movies
            raise AttributeError('Title not in this movie list')
        except:
            print('Enter a valid Title')

    # create a method that can creates the movie table in the nw database
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE Movies ({self.movies_list[0][0]} VARCHAR(255))")
        for heading in self.movies_list[0][1:]:
            self.cursor.execute(f"ALTER TABLE Movies ADD {heading} VARCHAR(255)")

    # create a method that can add movies as many movies to the database as user wants
    def add_movies(self):
        while True:
            try:
                row = self.search_title()
                # make row into a queriable string
                values = ", ".join(str(word) for word in row)
                self.cursor.execute(f"""
                    INSERT INTO Movies ({self.columns})
                    VALUES ('{values}');
                    """)
                check = input("add another movie to Movies? ")
                if check[0].lower() == 'n':
                    break
            except ValueError:
                print('something went wrong, please try again')

    # define a method that adds the whole table to the db, BEWARE OF DUBLICATES
    def add_all_movies_to_db(self):

        for row in self.movies_list[1:]:
            values = ", ".join(str(word) for word in row)
            self.cursor.execute(f"""
                INSERT INTO Movies ({self.columns})
                VALUES ('{values}');
                """)

    # Define a method that loads the db into an object (made abstract) (enter Movies as an argument)
    def load_object_from_db(self, table):
        try:
            obj_table = self.cursor.execute(f"SELECT * FROM {table}").fetchall()
            return obj_table
        except:
            print("please enter a table from northwind db")

    # Define a method that can output a table object to text file line by line (will be in a string format)
    def write_to_textfile(self, table):
        with open("imported_table.txt", 'w') as txtfile:
            for line in table:
                txtfile.write(", ".join(str(word) for word in line) + "\n")


# Now exectute functions in order of task
if __name__ == "__main__":
    ## ITERATION 1
    # get all the movies
    obj = MoviesDatabase('SA','Passw0rd2018') # establish connection and make class
    movies_list = obj.read_csv()

    # Search the movie by title
    print(obj.search_title())

    # Add whatever movies to the db
    obj.create_table()
    obj.add_movies()

    ## ITERATION 2
    #Save whole obj to db
    obj.add_all_movies_to_db()

    # load from db to obj
    new_obj = obj.load_object_from_db('Movies')

    # output object to text file
    obj.write_to_textfile(new_obj)
