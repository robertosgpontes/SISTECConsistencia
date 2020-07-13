from abc import ABC, abstractmethod

from pandas import DataFrame
from models import CursoCollections


class LoadCursoInterface(ABC):

    @abstractmethod
    def load(df: DataFrame) -> CursoCollections:
        pass
