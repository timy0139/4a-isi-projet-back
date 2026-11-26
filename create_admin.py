import getpass

from sqlmodel import Session, SQLModel, select

from database import engine
from models import User
from security import hash_password


def main():
    SQLModel.metadata.create_all(engine)
    username = input("Nom d'utilisateur admin : ").strip()
    password = getpass.getpass("Mot de passe admin : ")

    with Session(engine) as session:
        existant = session.exec(select(User).where(User.username == username)).first()
        if existant:
            print("Erreur : ce nom d'utilisateur existe déjà.")
            return

        admin = User(username=username, password=hash_password(password), is_admin=True)
        session.add(admin)
        session.commit()
        print(f"Administrateur '{username}' créé avec succès.")


if __name__ == "__main__":
    main()