from models.Curso import Curso


class CursoCollections:

    def __init__(self):
        self.curso_list = []

    def add(self, curso: Curso):
        self.curso_list.append(curso)
        return self

    @property
    def test(self):
        return self.curso_list[4]
