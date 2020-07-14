from functools import reduce

from models.Curso import Curso
import operator


class CursoCollection(list):

    def __init__(self, *args):
        #self.curso_list = []
        list.__init__(self, *args)

    #def add(self, curso: Curso):
    #    self.curso_list.append(curso)
     #   return self


# https://stackoverflow.com/questions/803616/passing-functions-with-arguments-to-another-function-in-python
