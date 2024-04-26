import pytest
from .connection import DBConnectionHandler


@pytest.mark.skip(reason="Sensive test")
def test_create_database_engine():
    db_conn_handle = DBConnectionHandler()

    engine = db_conn_handle.get_engine()

    assert engine is not None
