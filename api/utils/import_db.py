import sqlite3
from pathlib import Path
from sqlalchemy import text
from api.database.db import engine


def import_sql_file(sql_file_path: str) -> None:
    """
    Import SQL file into SQLite database using SQLAlchemy engine.

    Args:
        sql_file_path: Path to the SQL file to import
    """
    sql_file = Path(sql_file_path)

    if not sql_file.exists():
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")

    # Read the SQL file
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_content = f.read()

    # Execute the SQL content
    with engine.connect() as connection:
        # Split by semicolon and execute each statement
        statements = [stmt.strip() for stmt in sql_content.split(';') if stmt.strip()]

        for statement in statements:
            try:
                connection.execute(text(statement))
                print(f"✓ Executed: {statement[:50]}...")
            except Exception as e:
                print(f"✗ Error executing statement: {e}")

        # Commit the transaction
        connection.commit()
        print("\n✓ All SQL statements imported successfully!")


if __name__ == "__main__":
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    # Construct the path to the SQL file relative to this script
    sql_file_path = script_dir / "dump" / "airports.sql"
    
    # Import the airports.sql file
    import_sql_file(str(sql_file_path))