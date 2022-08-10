import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
import pyarrow
from os.path import join, dirname
from dotenv import load_dotenv
import time as time

os.chdir('/Users/danielrojaschacon/Documents')
dotenv_path = join(dirname('snowflake'),'snowflake.env')


load_dotenv(dotenv_path)
 # Get the credentials from .env
env_variables={
    'SF_ACCOUNT'    : os.getenv('SF_ACCOUNT'),
    'SF_USER'       : os.getenv('SF_USER'),
    'SF_WAREHOUSE'  : os.getenv('SF_WAREHOUSE'),
    'SF_DATABASE'   : os.getenv('SF_DATABASE'),
    'SF_SCHEMA'     : os.getenv('SF_SCHEMA'),
    'SF_PASSWORD'   : os.getenv('SF_PASSWORD'),
    'SF_ROLE'   : os.getenv('SF_ROLE')
}


def conection_write(df,table,env_variables):
    ctx = snowflake.connector.connect(
    user=env_variables['SF_USER'],
    password=env_variables['SF_PASSWORD'],
    account=env_variables['SF_ACCOUNT'],
    warehouse=env_variables['SF_WAREHOUSE'],
    database=env_variables['SF_DATABASE'],
    schema=env_variables['SF_SCHEMA'],
    role= env_variables['SF_ROLE']  
    )
    database=env_variables['SF_DATABASE']
    schema=env_variables['SF_SCHEMA']
    success, nchunks, nrows, _=write_pandas(ctx,df,table,database,schema)
    ctx.close()

def load_data(env_variables):
    start=time.time()
    xlsx = pd.ExcelFile('Matriculas.xlsx')
    df=pd.read_excel(xlsx, sheet_name='Matricula')
    df=df.assign(YEAR=df["AÑO"])
    df=df.drop(["NIVEL_CINE","AREA_UNESCO","DISCIPLINA_UNESCO","ZONA_DE URBANIZACION_ESTUDIANTE","ZONA_URBANO_RURAL_ESTUDIANTE","REGION_PLANIFICACION_ESTUDIANTE","CONTINENTE","AÑO"],axis=1)
    end=time.time()
    print('Load Excel in:',end-start,'s')
    start=time.time()
    df2=pd.read_csv('DIPLOMAS.csv')
    df2=df2.assign(YEAR=df2["AÑO"])
    df2=df2.drop(["AREA_UNESCO","DISCIPLINA_UNESCO","AREA_CANBERRA","ZONA_DE URBANIZACION_GRADUADO","ZONA_URBANO_RURAL_GRADUADO","REGION_PLANIFICACION_GRADUADO","CONTINENTE","AÑO"],axis=1)
    end=time.time()
    print('Load CSV in:',end-start,'s')
    
    start=time.time()
    conection_write(df,'MATRICULADOS',env_variables)
    end=time.time()
    print('Send 1st DF in:',end-start,'s')

    start=time.time()
    conection_write(df2,'EGRESADOS',env_variables)
    end=time.time()
    print('Send 2nd DF in:',end-start,'s')

if __name__ == "__main__":

    load_data(env_variables)

     