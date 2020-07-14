import math


class Curso:

    def __init__(self, descricao_eixo_tecnologico, codigo, nome, data_deferimento, codigo_tipo, descricao_tipo,
                 codigo_tipo_nivel, descricao_tipo_nivel, eh_experimental):
        self.descricao_eixo_tecnologico = descricao_eixo_tecnologico
        self.__codigo = codigo
        self.__nome = nome
        self.__data_deferimento = data_deferimento
        self.__codigo_tipo = codigo_tipo
        self.__descricao_tipo = descricao_tipo
        self.__codigo_tipo_nivel = codigo_tipo_nivel
        self.__descricao_tipo_nivel = descricao_tipo_nivel
        self.__eh_experimental = eh_experimental

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao_eixo_tecnologico(self):
        return self.__descricao_eixo_tecnologico

    @descricao_eixo_tecnologico.setter
    def descricao_eixo_tecnologico(self, var):
        self.__descricao_eixo_tecnologico = var
        if isinstance(var, float) and math.isnan(float(var)):
            self.__descricao_eixo_tecnologico = ''

        return self

    def __str__(self):
        return '{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8}\n'.format(
            self.__codigo,
            self.__nome,
            self.__data_deferimento,
            self.__descricao_eixo_tecnologico,
            self.__codigo_tipo,
            self.__descricao_tipo,
            self.__codigo_tipo_nivel,
            self.__descricao_tipo_nivel,
            self.__eh_experimental)

    def __add__(self, other):
        return self.__str__() + str(other)

