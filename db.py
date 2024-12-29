from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL

Base = declarative_base()

url_postgres = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="postgres",
    port=5432
)

engine_postgres = create_engine(url_postgres)

try:
    with engine_postgres.connect() as conn:
        conn.execute(text("COMMIT"))
        conn.execute(text("CREATE DATABASE artdb"))
        print("Database 'artdb' created successfully!")
except Exception as e:
    print(f"Error creating database: {e}")

url_artdb = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="artdb",
    port=5432
)
engine_artdb = create_engine(url_artdb)

try:
    with engine_artdb.connect() as conn:
        conn.execute(text("ALTER DATABASE artdb OWNER TO postgres"))
        print("Database owner set to 'postgres'")
except Exception as e:
    print(f"Error setting owner: {e}")

try:
    Base.metadata.create_all(bind=engine_artdb)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")
