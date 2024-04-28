from typing import List

from src.infra.db.settings.connection import DBConnectionHandler
from src.domain.entities.users import Users as UsersEntity
from src.app.data.interfaces.users_repository import (
    UsersRepository as UsersRepositoryInteface,
)
from src.domain.models.users import Users


# UsersRepository precisa da interface para informar os metodos obrigatórios
class UsersRepository(UsersRepositoryInteface):

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

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as err:
                database.session.rollback()
                return err
