from abc import ABC, abstractmethod
from typing import Dict

# Use Cases == Funcionalides
# UserFinder (Interface) diz o que é necessário para buscar users.


class UserFinder(ABC):
    @abstractmethod
    def find(self, first_name: str) -> Dict:
        pass
