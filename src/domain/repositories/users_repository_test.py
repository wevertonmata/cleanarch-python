from typing import List
from random import randint
import pytest
from faker import Faker
from sqlalchemy import text

from src.domain.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UsersRepository

db_conn_handler = DBConnectionHandler()
conn = db_conn_handler.get_engine().connect()


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    fake = Faker(["pt_BR"])
    mocked_first_name = fake.unique.first_name()
    mocked_last_name = fake.unique.last_name()
    mocked_age = randint(1, 100)

    users_repository = UsersRepository()
    users_repository.insert_user(
        mocked_first_name, mocked_last_name, mocked_age
    )

    sql = f"""
        SELECT * FROM users
        WHERE first_name = '{mocked_first_name}'
        AND last_name = '{mocked_last_name}'
        AND age = '{mocked_age}'
    """
    resp = conn.execute(text(sql))
    registry: UsersEntity = resp.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    conn.execute(
        text(
            f"""
        DELETE FROM users WHERE id = {registry.id}
    """
        )
    )
    conn.commit()


@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    fake = Faker(["pt_BR"])
    mocked_first_name = fake.unique.first_name()
    mocked_last_name = fake.unique.last_name()
    mocked_age = randint(1, 100)

    sql = f"""
        INSERT INTO users (first_name, last_name, age)
        VALUES ('{mocked_first_name}', '{mocked_last_name}', '{mocked_age}' )
    """

    conn.execute(text(sql))
    conn.commit()

    users_repository = UsersRepository()
    response: List[UsersEntity] = users_repository.select_user(mocked_first_name)  # type: ignore

    assert response[0].first_name == mocked_first_name
    assert response[0].last_name == mocked_last_name
    assert response[0].age == mocked_age

    conn.execute(
        text(
            f"""
        DELETE FROM users WHERE id = {response[0].id}
    """
        )
    )
    conn.commit()
