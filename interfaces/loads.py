from abc import ABC, abstractmethod

from pandas import DataFrame
from models import CursoCollection


class LoadCursoInterface(ABC):

    @abstractmethod
    def load(df: DataFrame) -> CursoCollection:
        pass
