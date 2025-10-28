import pymysql as mysql

# Step 1: Connect to MySQL server (no DB yet) to create the database
conn = mysql.connect(
    host='localhost',
    user='root',
    password=''
)
cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS db_Aptech")
conn.close()  # Close initial connection

# Step 2: Reconnect with the newly created database
conn = mysql.connect(
    host='localhost',
    user='root',
    password='',
    db='db_Aptech'
)
cursor = conn.cursor()

# Multi-line string literals: Line breaks, indentation and spacing are kept exactly as written.
# Step 3: Create table with correct syntax
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_students (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Std_name VARCHAR(50),
    Std_age INT,
    Std_batch VARCHAR(50),
    Std_lab VARCHAR(50)
)
""")

# Step 4: Insert student data
def Insertdata():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    batchcode = input("Enter student batchcode: ")
    lab = input("Enter student lab: ")

    query = """
    INSERT INTO tbl_students (Std_name, Std_age, Std_batch, Std_lab)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, age, batchcode, lab))
    conn.commit()
    print("✅ Student data added successfully.\n")

Insertdata()

# Step 5: Fetch and display all student records
def Fetchdata():
    cursor.execute("SELECT * FROM tbl_students")
    data = cursor.fetchall()
    print("📋 All Student Data:")
    for row in data:
        print(row)
    print()

Fetchdata()

# Step 6: Delete a student by ID
def Deletedata():
    sid = int(input("Enter student ID to delete: "))
    query = "DELETE FROM tbl_students WHERE Id = %s"
    cursor.execute(query, (sid,))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Student data deleted successfully.\n")
    else:
        print("⚠️ Student not found.\n")

Deletedata()

# Step 7: Update student name by ID
def Updatedata():
    sid = int(input("Enter student ID to update: "))
    name = input("Enter new student name: ")
    age = input("Enter new student age: ")
    batch = input("Enter new student batch: ")
    lab = input("Enter new student lab: ")

    # ✅ Corrected SQL syntax with commas between column updates
    query = "UPDATE tbl_students SET Std_name = %s, Std_age = %s, Std_batch = %s, Std_lab = %s WHERE Id = %s"
    cursor.execute(query, (name, age, batch, lab, sid))
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Student data updated successfully.\n")
    else:
        print("⚠️ Student not found.\n")

Updatedata()