from abc import ABC

from interfaces.loads import LoadCursoInterface

from pandas import DataFrame

from models.Curso import Curso
from models.CursoCollections import CursoCollections


class LoadCurso(LoadCursoInterface, ABC):

    @staticmethod
    def load(df: DataFrame) -> CursoCollections:
        curso_collection = CursoCollections()
        for curso in LoadCurso.__prepare_data(df=df).values:
            if curso[8] == 'SIM':
                eh_experimental = True
            else:
                eh_experimental = False

            curso_collection.add(
                Curso(
                    descricao_eixo_tecnologico=curso[0],
                    codigo=curso[1],
                    nome=curso[2],
                    data_deferimento=curso[3],
                    codigo_tipo=curso[4],
                    descricao_tipo=curso[5],
                    codigo_tipo_nivel=curso[6],
                    descricao_tipo_nivel=curso[7],
                    eh_experimental=eh_experimental
                ))

        return curso_collection

    @staticmethod
    def __prepare_data(df: DataFrame) -> DataFrame:
        return df[['ds_eixo_tecnologico', 'co_curso', 'no_curso', 'dt_deferimento_curso',
                   'co_tipo_curso', 'tipo_curso', 'co_tipo_nivel', 'ds_tipo_nivel',
                   'experimental', ]].drop_duplicates()
