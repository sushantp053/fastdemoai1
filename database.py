from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///demo.db"
# DATABASE_URL = "postgresql+driver://user:password@host:port/dbname"
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
