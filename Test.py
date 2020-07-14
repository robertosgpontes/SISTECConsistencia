import pandas as pd

from consistency_rules.PNP2020 import CursoConsistencyRules
from models.CursoCollection import CursoCollection
from utils.LoadCurso import LoadCurso

sistec = pd.read_excel('dataset/dados_if.xlsx', skiprows=[0])

cursos = LoadCurso.load(sistec)

curso_consistencia = CursoConsistencyRules(cursos)

cursos_com_nome_improprio = CursoCollection(curso_consistencia.cursosNomeImproprio())


print(len(cursos))
print(len(cursos_com_nome_improprio))