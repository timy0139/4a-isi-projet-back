import os
from sqlalchemy import event
from sqlmodel import Session, create_engine

# si pas de variable d'env => base sqlite en local
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./local.db")

# False obligatoir sinon erreur sur les threads
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@event.listens_for(engine, "connect")
def activer_cles_etrangeres(dbapi_connection, _):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


def get_session():
    with Session(engine) as session:
        yield session