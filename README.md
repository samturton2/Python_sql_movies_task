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