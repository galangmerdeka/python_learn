from itertools import count
import json
from msilib import sequence
from turtle import st
import psycopg2 as pg
import pandas as pd
import sqlalchemy as sql_dml
import os

schema_json = 'D:/Python/python_learn/project_3/schemas/user_address.json'
create_schema_sql = """create table user_address_2018_snapshots {};"""
data_set_csv_medium = 'D:/Python/python_learn/project_3/temp/dataset-medium.csv'
database = 'shipping_orders'
user = 'postgres'
password = 'admin'
host_conn='127.0.0.1'
port_conn='5432'
table_name = 'user_address_2018_snapshots'
truncate_scripts = """truncate table {};"""
count_scripts = """SELECT COUNT(*) FROM {};"""
data_part_dir = 'D:/Python/python_learn/project_3/temp/data_part/'

# load schema from json
with open(schema_json, 'r') as schema:
    content = json.loads(schema.read())

list_schema = []
for c in content:
    col_name = c['column_name']
    col_type = c['column_type']
    constraint = c['is_null_able']
    ddl_list = [col_name, col_type, constraint]
    list_schema.append(ddl_list)

list_schema2 = []
for l in list_schema:
    s = ' '.join(l)
    list_schema2.append(s)

create_schema_sql_final = create_schema_sql.format(tuple(list_schema2)).replace("'", "")
# create_truncate_schema = truncate_scripts.format(table_name)

# print(create_schema_sql_final)
# write the final schema sql into file .sql
try:
    with open('D:/Python/python_learn/project_3/sql/ddl/ddl_user_address_ddl.sql', 'w') as sql_file:
        sql_file.write(create_schema_sql_final)
        # print(create_truncate_schema)
        print("The file .sql has been created")
except FileNotFoundError:
    print("The docs or directory does not exists")

# Connect to database - postgree

conn = pg.connect(
    database=database,
    user=user,
    password=password,
    host=host_conn,
    port=port_conn
)

conn.autocommit = True
cursor = conn.cursor()

try:
    cursor.execute(create_schema_sql_final)
    print("DDL schema created...")
except pg.errors.DuplicateTable:
    cursor.execute(truncate_scripts.format(table_name))
    print("Table already created...")
    print("Data on the table exist are Truncated...")

# split the data into part 1-10
rowsize = 30000

# load from dataset medium .csv
df = pd.read_csv(
    data_set_csv_medium, 
    header=None
)

col_name_df = [c['column_name'] for c in content]
df.columns = col_name_df

# print(df.columns)

# get the numbers of line from csv
numb_lines = sum(1 for row in (open(data_set_csv_medium)))
print(f'total rows data : {numb_lines}')

# def numbers():
#     for filename in counter_file.listdir('D:/Python/python_learn/project_3/temp/data_part/'):
#             name, _ = counter_file.path.splitext()
#             yield int(name[4:])

# start looping and writing it into file
try:
    print("Creating file csv per part...")
    for i in range(1, numb_lines, rowsize):
        df = pd.read_csv(
                    data_set_csv_medium, 
                    header=None,
                    nrows=rowsize,
                    skiprows=i
                )
        # csv to write data to a new file
        
        # count = max(numbers)
        # count += 1
        # print(f'file {count}')

        file_res = '../temp/data_part/data-part-'+str(i)+'.csv'
        print(file_res)
        result = df.to_csv(
            file_res,
            header=False,
            index=False,
            mode='a',
            chunksize=rowsize
        )
    # file_output.write(result)
except:
    print("Something went wrong")

# load from data set from data-part directory
try:
    engine = sql_dml.create_engine(f'postgresql://{user}:{password}@{host_conn}:{port_conn}/{database}')
    for path in os.listdir(data_part_dir):
        full_path = os.path.join(data_part_dir, path)
        if os.path.isfile(full_path):
            df = pd.read_csv(full_path, header=None)
            col_name_df = [c['column_name'] for c in content]
            df.columns = col_name_df
            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            
            print("LOG INSERT DATA PER PART")
            print(f'Total inserted row : {len(df)}')
            # print(f'Job is finished. table {table_name} has {i[0]}')
            # print(f'Job is finished. table {table_name} has {number} rows and last created_at is {df.crated_at.max()}')
            print("-------------------------")
except:
    print("Read file on the directory failed..")