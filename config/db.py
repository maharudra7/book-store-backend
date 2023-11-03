from sqlmodel import SQLModel, create_engine

postgres_url = "postgresql://szjjehfu:eQVBoa_WfDjZ0xUjWp5PvFldhzz6BHKh@tiny.db.elephantsql.com/szjjehfu"

engine = create_engine(postgres_url)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)