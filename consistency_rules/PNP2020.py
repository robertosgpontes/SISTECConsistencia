from models.Curso import Curso
from models.CursoCollection import CursoCollection


class CursoConsistencyRules:
    __NOMES_IMPROPRIOS = ['SEMINÁRIO', 'ENCONTRO', 'OLIMPÍADA', 'AÇÃO SOLIDÁRIA', 'AÇÕES SOLIDÁRIAS', 'PALESTRA',
                          'CERIMÔNIA', 'SEMANA', 'TERTÚLIA', 'CAVALGADA', 'JORNADA', 'EXPERIÊNCIA', 'FÓRUM', 'FORUNS',
                          'CIRCUITO', 'VISITA', 'CONCURSO', 'TREINAMENTO', 'SIMPÓSIO', 'CICLO', 'APRESENTAÇÃO',
                          'APRESENTAÇÕES', 'GINCANA', 'FESTIVAL', 'FESTIVAIS', 'CINEMA', 'COMENTADO', 'CURTINDOOBMEP',
                          'FEIRA', 'DIA DE CAMPO', 'DIAS DE CAMPOS', 'DIAS DE CAMPO', 'IFSHOW', 'EMPREENTEC',
                          'CIRCUITO', 'AMAZON AWS', 'BUSCA', 'CHAMADA', 'EXPOSIÇÃO', 'EXPOSIÇÕES', 'VOLEIBOL',
                          'TÉCNICO']

    def __init__(self, curso_collection: CursoCollection):
        self.__curso_collection = curso_collection

    def cursosNomeImproprio(self) -> CursoCollection:
        """
        Nenhum curso pode conter em seu nome as palavras nem no plural e nem no singular: seminário, encontro,
        olimpíada, açãosolidária, palestra,cerimônia, semana,tertúlia, cavalgada,jornada, experiência,fórum, circuito,
        visita,concurso,treinamento, simpósio, ciclo, apresentação,gincana, festival,cinema comentado,#CURTINDOOBMEP,
        feira, dia de campo, IFshow, EMPREENTEC,circuito, AMAZON AWS, busca, chamada,exposição e voleibol.

        @return:

        """

        def rule(curso: Curso):
            return any(nome in curso.nome for nome in self.__NOMES_IMPROPRIOS)

        return filter(rule, self.__curso_collection)
