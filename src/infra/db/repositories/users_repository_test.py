from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository


def test_insert_user():
    mocked_first_name = "weverton"
    mocked_last_name = "mata"
    mocked_age = 21

    users_repository = UsersRepository()
    users_repository.insert_user(
        mocked_first_name, mocked_last_name, mocked_age
    )


# pytest -s -v src\infra\db\repositories\users_repository_test.py
