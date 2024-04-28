from typing import Dict

from src.app.data.interfaces.users_repository import (
    UsersRepository as UsersRepositoryInteface,
)
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface


# Para buscar um usuário eu preciso eu preciso herdar interface do use_cases em domain que vai aplicar o contrato.
#
class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInteface):
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        pass
