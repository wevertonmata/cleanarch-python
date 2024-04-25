from sqlalchemy import create_engine


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = (
            "{Server}://{User}}:{Password}@{Host}:{Port}/{Database}".format(
                Server="mariadb+mariadbconnector",
                User="root",
                Password="root",
                Host="127.0.0.1",
                Port="3306",
                Database="clean_database",
            )
        )

        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine