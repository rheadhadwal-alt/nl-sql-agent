import sqlite3

def get_schema_description(db_path="Sample - Superstore.db"):
    """
    Inspects the SQLite database and returns a text description
    of its tables and columns, formatted for use in an LLM prompt.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema_lines = []
    for (table_name,) in tables:
        schema_lines.append(f"Table: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for col in columns:
            col_name = col[1]
            col_type = col[2]
            schema_lines.append(f"  - {col_name} ({col_type})")
        schema_lines.append("")  # blank line between tables

    conn.close()
    return "\n".join(schema_lines)


if __name__ == "__main__":
    print(get_schema_description())