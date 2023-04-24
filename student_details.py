import mysql.connector

# MySQL database connection details
host = "database-2.cs6abjlnipb5.eu-north-1.rds.amazonaws.com"
database = "college_cc"
user = "root"
password = "rootuser12345"

# Connect to the database
conn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

while True:
    # Prompt the user to enter student details
    name = input("Enter student name (or 'quit' to exit): ")
    if name == "quit":
        break
    age = int(input("Enter student age: "))
    gender = input("Enter the gender - Male or Female: ")
    stud_class = int(input("Enter the student class from 1 to 9: "))
    favourite_sub = input("Enter student's Favourite Subject: ")

    # Insert the student details into the database
    cursor = conn.cursor()
    sql = "INSERT INTO new_table (Name, Age, Gender, Class, Favourite_subject) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age,gender, stud_class,favourite_sub)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()

print("-------Student details inserted successfully!--------")
# Close the database connection
conn.close()