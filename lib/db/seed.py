# lib/db/seed.py

from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Sample authors
    authors = [
        ("Alice Walker",),
        ("George Orwell",),
        ("Maya Angelou",)
    ]

    # Sample magazines
    magazines = [
        ("The New Yorker", "Literature"),
        ("Tech Monthly", "Technology"),
        ("Global Times", "Politics")
    ]

    # Sample articles (title, author_id, magazine_id)
    articles = [
        ("The Color of Thought", 1, 1),
        ("Big Brother Rewired", 2, 2),
        ("Poetry in Motion", 3, 1),
        ("AI and Ethics", 1, 2),
        ("Freedom and Power", 2, 3),
        ("Rise of the Machines", 2, 2),
    ]

    # Insert into tables
    cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)
    cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)
    cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)

    conn.commit()
    conn.close()
    print("✅ Seed data inserted.")

# Run this script directly
if __name__ == "__main__":
    seed_data()
