import pandas as pd

from models.CursoCollections import CursoCollections
from utils.LoadCurso import LoadCurso

arq_campus_if = pd.read_excel('dataset/dados_if.xlsx', skiprows=[0])

a = LoadCurso.load(arq_campus_if)

print(a.test)
