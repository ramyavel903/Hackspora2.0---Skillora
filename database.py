import sqlite3

DATABASE = "scamcheck.db"
def create_database():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            opportunity_type TEXT,
            email TEXT,
            website TEXT,
            description TEXT,
            payment TEXT,
            score INTEGER,
            risk_level TEXT,
            warnings TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(
    company,
    opportunity_type,
    email,
    website,
    description,
    payment,
    score,
    risk_level,
    warnings
):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses (
            company,
            opportunity_type,
            email,
            website,
            description,
            payment,
            score,
            risk_level,
            warnings
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        company,
        opportunity_type,
        email,
        website,
        description,
        payment,
        score,
        risk_level,
        "\n".join(warnings)
    ))

    connection.commit()
    connection.close()
