from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="postgres", 
    port=5432
)

engine = create_engine(url)

from sqlalchemy import text

with engine.connect() as conn:
    conn.execute(text("COMMIT"))
    conn.execute(text("CREATE DATABASE artdb"))

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="postgres",
    host="localhost",
    database="artdb",  
    port=5432
)
engine = create_engine(url)

with engine.connect() as conn:
    conn.execute(text("ALTER DATABASE artdb OWNER TO postgres"))

Base.metadata.create_all(bind=engine)

print("DataBases are successfully created!")
