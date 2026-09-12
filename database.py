import sqlite3
import os

DB_PATH = "data/campus.db"


def connect_db():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)
def create_tables():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint_id TEXT UNIQUE,
            student_name TEXT NOT NULL,
            department TEXT,
            building TEXT,
            room_no TEXT,
            category TEXT,
            problem TEXT NOT NULL,
            priority TEXT,
            status TEXT,
            date TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maintenance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            complaint_id TEXT,
            staff_name TEXT,
            repair_date TEXT,
            cost REAL,
            remarks TEXT
        )
    """)

    conn.commit()
    conn.close()
def complaint_exists(complaint_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT complaint_id
        FROM complaints
        WHERE complaint_id = ?
    """, (complaint_id,))

    result = cursor.fetchone()

    conn.close()

    return result is not None

def add_maintenance(
    complaint_id,
    staff_name,
    repair_date,
    cost,
    remarks
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO maintenance (
            complaint_id,
            staff_name,
            repair_date,
            cost,
            remarks
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        complaint_id,
        staff_name,
        repair_date,
        cost,
        remarks
    ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database created successfully!")

def generate_complaint_id():    
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM complaints")
    count=cursor.fetchone()[0]

    conn.close()

    return f"CMP{count + 1:03d}"

def add_complaint(
    student_name,
    department,
    building,
    room_no,
    category,
    problem,
    priority,
    date
):
    conn = connect_db()
    cursor = conn.cursor()

    complaint_id = generate_complaint_id()

    cursor.execute("""
        INSERT INTO complaints (
            complaint_id,
            student_name,
            department,
            building,
            room_no,
            category,
            problem,
            priority,
            status,
            date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        complaint_id,
        student_name,
        department,
        building,
        room_no,
        category,
        problem,
        priority,
        "Pending",
        date
    ))

    conn.commit()
    conn.close()

    return complaint_id

def get_all_complaints():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            complaint_id,
            student_name,
            category,
            building,
            priority,
            status,
            date
        FROM complaints
        ORDER BY id DESC
    """)

    complaints = cursor.fetchall()

    conn.close()

    return complaints
def search_complaint(complaint_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            complaint_id,
            student_name,
            department,
            building,
            room_no,
            category,
            problem,
            priority,
            status,
            date
        FROM complaints
        WHERE complaint_id = ?
    """, (complaint_id,))

    complaint = cursor.fetchone()

    conn.close()

    return complaint

def get_complaint_status(complaint_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status
        FROM complaints
        WHERE complaint_id = ?
    """, (complaint_id,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def update_complaint_status(complaint_id, new_status):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE complaints
        SET status = ?
        WHERE complaint_id = ?
    """, (new_status, complaint_id))

    conn.commit()

    rows_updated = cursor.rowcount

    conn.close()

    return rows_updated

