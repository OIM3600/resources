# Hall of Prophecy

## Getting Started

1. On GitHub Desktop, make sure your current repository is `OIM3600`. Then click `Repository` -> `Open in Visual Studio Code` to open the folder in your **VS Code**.
2. In VS Code, create a new folder `prophecy`. Then, under `prophecy` folder, create `scheme.sql` and `prophecy.py`.
3. Download `roster.db` file from [`roster.db`](./prophecy/roster.db) on GitHub. Download `students.csv` file from [`students.csv`](./prophecy/students.csv) on GitHub. Copy the downloaded files, `roster.db` and `students.csv` into the `data` folder, which should be inside the main `OIM3600` folder. 

## Learning Goals

- “Refactor” a SQL database to eliminate redundancies
- Use `SELECT`, `CREATE`, and `INSERT` statements to reorganize data
- Write Python to load new SQL tables


## Background

The keeper of [the Hall of Prophecy](https://harrypotter.fandom.com/wiki/Hall_of_Prophecy), whose job entailed labelling records and keeping them up to date, decided to create a SQL database of Hogwarts students. Unfortunately the database was poorly designed! The database, `roster.db`, contains only one table, `students`, with the name and head of each of the four Hogwarts Houses.

Stumbling upon this database, you decide it could be better designed. Take a look at `roster.db` and notice how the name and head of each house repeats over and over. A better design would contain a students table (for *only* students), a houses table (for *only* houses), and a table that codifies the relationship between students and houses. This process of changing the “schema” of a database is known as [refactoring](https://en.wikipedia.org/wiki/Database_refactoring).


<details>
<summary>Hints:</summary>
- You can view the data in the Hall of Prophecy’s table by executing `sqlite3 roster.db`, followed by `.schema` in your `sqlite3` prompt. This will output the `CREATE TABLE` statement that was used to generate the `students` table.
You can then use `SELECT` statements to view the contents of this table.
</details>


## Implementation Details

You will use the existing data in roster.db to create a new database, one with a table for students, a table for houses, and a table for house assignments. You can do this with individual `SQL` queries, though we recommend ultimately writing your own Python program to automate the process! Notice we’ve given you the data from the students table of `roster.db` in CSV format, `students.csv`, for your convenience.


### Developing a Schema

First, let’s develop a new schema for the database. In `schema.sql`, document the three `CREATE TABL`E commands you’ll need to create your three new tables.

Keep in mind you’ll want each table to represent a single entity: that is, your students table should represent *only* students, your houses table should represent *only* houses, and your house assignments table should represent *only* house assignments. You might find it helpful to first consider the pieces of information you’ll need in each table, and then about which SQLite data type best represents that information. For example, this was the `CREATE TABLE` command for `students`:
```sql
CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);
```

Keep in mind that every table should have a primary key: a column that uniquely identifies every row in the table. Some tables may be best designed with foreign keys: columns that reference the primary keys of another table.

When you’re ready to configure your database with your new schema, run your three new `CREATE TABLE` queries. Type `.schema` to see your results.

### Inserting Data

After you’ve configured your database with your new schema, you can begin inserting data into your new database (using your new schema!). It’s best to write a Python program (`prophecy.py`) here, which can save you the trouble of writing many `INSERT` queries. Keep in mind that you have `students.csv`, which contains the data from the previous database’s students table.

## Thought Question

- Why do you think it’s considered better design not to repeat information like houses and heads for each student?


# How to Submit

- Save all the files opened in VS Code. Format your code before saving.
- **Commit** and **Push to Origin** in GitHub Desktop. Check repository on GitHub.com to make sure all the commits are successfully pushed to remote.
