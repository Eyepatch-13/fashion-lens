import sqlite3
import csv
import os

def create_database(csv_path, db_path):
    """
    Creates an SQLite database from a CSV file.

    Args:
        csv_path (str): Path to the styles.csv file.
        db_path (str): Path to the SQLite database file to be created.
    """
    # Connect to SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the products table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            gender TEXT,
            masterCategory TEXT,
            subCategory TEXT,
            articleType TEXT,
            baseColour TEXT,
            season TEXT,
            year INTEGER,
            usage TEXT,
            productDisplayName TEXT
        )
    """)

    # Read the CSV file and insert data into the database
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        # Prepare the SQL statement for insertion
        insert_query = """
            INSERT INTO products (id, gender, masterCategory, subCategory, articleType,
                                  baseColour, season, year, usage, productDisplayName)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        count = 0
        # Insert rows from the CSV file
        for row in reader:
            cursor.execute(insert_query, (
                int(row['id']),
                row['gender'],
                row['masterCategory'],
                row['subCategory'],
                row['articleType'],
                row['baseColour'],
                row['season'],
                int(row['year']),
                row['usage'],
                row['productDisplayName']
            ))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database created successfully at {db_path}")

if __name__ == "__main__":
    # Define the paths
    csv_path = os.path.join("instance", "styles.csv")
    db_path = os.path.join("instance", "products.db")
    
    # Create the database
    create_database(csv_path, db_path)
