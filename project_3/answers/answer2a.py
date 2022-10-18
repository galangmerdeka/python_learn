import json
import psycopg2 as pg
import pandas as pd
import sqlalchemy as sql_dml

# D:\Python\python_learn\project_3\schemas
schema_json = 'D:/Python/python_learn/project_3/schemas/user_address.json'
create_schema_sql = """create table user_address_2018_snapshots {};"""
data_set_csv = 'D:/Python/python_learn/project_3/temp/dataset-small.csv'
database = 'shipping_orders'
user = 'postgres'
password = 'admin'
host_conn='127.0.0.1'
port_conn='5432'
table_name = 'user_address_2018_snapshots'

# load schema from json file
with open(schema_json, 'r') as schema:
    content = json.loads(schema.read())

# print(content)

list_schema = []
for c in content:
    col_name = c['column_name']
    col_type = c['column_type']
    constraint = c['is_null_able']
    ddl_list = [col_name, col_type, constraint]
    list_schema.append(ddl_list)

# print(list_schema)

list_schema2 = []
for l in list_schema:
    s = ' '.join(l)
    list_schema2.append(s)

# print(list_schema2)

create_schema_sql_final = create_schema_sql.format(tuple(list_schema2)).replace("'", "")
# print(create_schema_sql_final)

# Connect to database - postgree
conn = pg.connect(
    database = database,
    user=user,
    password=password,
    host=host_conn,
    port=port_conn
)

conn.autocommit = True
cursor = conn.cursor()

try:
    # cursor.connection()
    # print("connection succesfull")
    cursor.execute(create_schema_sql_final)
    print("DDL schema created...")
except pg.errors.DuplicateTable:
    print("Table already created..")

# load from dataset.csv
df = pd.read_csv(data_set_csv, header=None)

col_name_df = [c['column_name'] for c in content]
df.columns = col_name_df

# print(df.columns)

df_filtered = df[(df['created_at'] >= '2018-02-01') & (df['created_at'] < '2018-12-31')]

# print(df_filtered)

# create engine
engine = sql_dml.create_engine(f'postgresql://{user}:{password}@{host_conn}:{port_conn}/{database}')
# sama seperti postgresql://postgres:admin@localhost:5432/shipping_orders

# insert data
df_filtered.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# log insert data
print("LOG INSERT DATA")
print(f'Total inserted row : {len(df_filtered)}')
print(f'Initial created at : {df_filtered.created_at.min()}')
print(f'Last created at : {df_filtered.created_at.max()}')