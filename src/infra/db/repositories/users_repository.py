from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConnectionHandler() as database:
            try:
                insert_query = UsersEntity(
                    first_name=first_name, last_name=last_name, age=age
                )

                database.session.add(insert_query)
                database.session.commit()
            except Exception as err:
                database.session.rollback()
                return err
