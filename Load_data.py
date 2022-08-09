import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
import pyarrow
from os.path import join, dirname
from dotenv import load_dotenv

os.chdir('/Users/danielrojaschacon/Documents')
dotenv_path = join(dirname('snowflake'),'snowflake.env')


load_dotenv(dotenv_path)
 # Get the credentials from .env
SF_ACCOUNT    = os.getenv('SF_ACCOUNT')
SF_USER       = os.getenv('SF_USER')
SF_WAREHOUSE  = os.getenv('SF_WAREHOUSE')
SF_DATABASE   = os.getenv('SF_DATABASE')
SF_SCHEMA     = os.getenv('SF_SCHEMA')
SF_PASSWORD   = os.getenv('SF_PASSWORD')
SF_ROLE   = os.getenv('SF_ROLE')


def load_data():
    xlsx = pd.ExcelFile('Matriculas.xlsx')
    df=pd.read_excel(xlsx, sheet_name='Matricula')

    df=df.assign(YEAR=df["AÑO"])
    df=df[["YEAR","TIPO_MATRICULA","UNIVERSIDAD","SEDE_CONARE","TIPO_SEDE","REGION_PLANIFICACION_SEDE","CARRERA","GRADO_ACADEMICO","NIVEL_ACADEMICO","AREA_CONOCIMIENTO",
    "DISCIPLINA","STEM_MICITT","SEXO","EDAD","PROVINCIA_ESTUDIANTE","CANTON_ESTUDIANTE","DISTRITO_ESTUDIANTE",
    "PAIS_ESTUDIANTE","TIPO_NACIONALIDAD"]] 
    
    print(df.head(5))

    

if __name__ == "__main__":

    load_data()

 #FILTER
#df_cor.info()
#df_cor
#df_cor = df_cor.drop(df_cor[df_cor.PROVINCIA_GRADUADO =='Sin Información'].index) 
#df_cor = df_cor.drop(df_cor[df_cor.PROVINCIA_GRADUADO =='Sin información'].index)

#df_cor = df_cor.drop(df_cor[df_cor.CANTON_GRADUADO =='Sin Información'].index) 
#df_cor = df_cor.drop(df_cor[df_cor.CANTON_GRADUADO =='Sin información'].index) 

##df_cor = df_cor.drop(df_cor[df_cor.DISTRITO_GRADUADO =='Sin Información'].index) 
##df_cor = df_cor.drop(df_cor[df_cor.DISTRITO_GRADUADO =='Sin información'].index) 
# print('----------------------------------------------------------------------------------')
# df_cor.info()
# df_cor       