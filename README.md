# SQL Movies CRUD

## Task
#### Summary
Now that you've learned how to connect to the DB using pyodbc you can start abstracting out interaction the db! This is great if you don't like writing sql.

#### Tasks
- CRUD the DB
Hint: create abstraction and methods to deal with db so you don't have too

#### Acceptance Criteria
- You can get all the movies
- you can search based on title
- you can add movies to DB

### second iteration:
- IMDB CSV <> Py <> SQL
#### Summary
You know how to parse txt files into python.
You also know how to connect python into the db.
You also know how to manipulated and change data with python.

Your task is to move data from text files into the db and from the the db into text files

#### Tasks
- read the text file and create object
- save object in DB
- Load that from DB and create object
- output object to text file

Extra:
* Explore other APIs

#### Acceptance Criteria
- able to take in 10 film names in text file and save to db
- able to load data from DB and create text file with names

### Task walkthrough
- make a new file
- Import pyodbc to connect with SQL
```python
import pyodbc
```
- import csv to help read the csv file
```python
import csv
```
- create class that can export data from csv file
```python
class MoviesDatabase:
```
- get a connection to the northwind database when you call the class
```python
    def __init__(self, username, password):
        self.username = username
        self.password = password
        server = "databases1.spartaglobal.academy"
        database = "Northwind"
        self.northwind_connection = pyodbc.connect(f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}')
        # create a class variable that's the cursor
        self.cursor = self.northwind_connection.cursor()
```
- create a function that loads each row as a list into a python list
```python
    def read_csv(self):
        self.movies_list = []
        with open("imdbtitles.csv", 'r') as csvfile:
            reader = csv.reader(csvfile) # stores each row as a list in a list (type is csv reader, so have to unpack it into a list)
            for row in reader:
                self.movies_list.append(row)
        # get rid of first 3 letters in movies titleType heading name manually
        self.movies_list[0][0] = self.movies_list[0][0][3:]
        # declare column titles as a string for queries
        self.columns = ", ".join(str(word) for word in self.movies_list[0])
        return self.movies_list
```

- Search movies list on title, bare in mind read_cvs module has to be called first
```python
    def search_title(self):
        title = input("What movie do you want? : ")
        try:
            for movies in self.movies_list:
                if movies[2].lower() == title.lower().strip():
                    return movies
            raise AttributeError('Title not in this movie list')
        except:
            print('Enter a valid Title')
```
- create a method that can creates the movie table in the nw database
```python
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE Movies ({self.movies_list[0][0]} VARCHAR(255))")
        for heading in self.movies_list[0][1:]:
            self.cursor.execute(f"ALTER TABLE Movies ADD {heading} VARCHAR(255)")
```

- create a method that can add movies as many movies to the database as user wants
```python
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
```
- define a method that adds the whole table to the db, BEWARE OF DUBLICATES
```python  
    def add_all_movies_to_db(self):
        # create a loop adding all rows other than the column titles
        for row in self.movies_list[1:]:
            values = ", ".join(str(word) for word in row)
            self.cursor.execute(f"""
                INSERT INTO Movies ({self.columns})
                VALUES ('{values}');
                """)
```
- Define a method that loads the db into an object (made abstract) (enter Movies as an argument)
```python    
    def load_object_from_db(self, table):
        try:
            obj_table = self.cursor.execute(f"SELECT * FROM {table}").fetchall()
            return obj_table
        except:
            print("please enter a table from northwind db")
```
- Define a method that can output a table object to text file line by line (will be in a string format)
```python    
    def write_to_textfile(self, table):
        with open("imported_table.txt", 'w') as txtfile:
            for line in table:
                txtfile.write(", ".join(str(word) for word in line) + "\n")
```

- Now exectute functions in order of task
```python
if __name__ == "__main__":
```
- ITERATION 1
- get all the movies
```python
    obj = MoviesDatabase('SA','Passw0rd2018') # establish connection and make class
    movies_list = obj.read_csv()
```
- Search the movie by title
```python
    print(obj.search_title())
```
- Add whatever movies to the db
```python
    obj.create_table()
    obj.add_movies()
```
- ITERATION 2
- Save whole obj to db
```python
    obj.add_all_movies_to_db()
```
- load from db to obj
```python
    new_obj = obj.load_object_from_db('Movies')
```
-  output object to text file
```python
    obj.write_to_textfile(new_obj)
```