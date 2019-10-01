import pandas as pd
import sqlite3
import statistics

conn = sqlite3.connect("db.sqlite3")
df = pd.read_sql_query("select * from Users;", conn)

df['full_name'] = pd.DataFrame(df['first_name'] + " " + df['last_name'])
df.to_excel("db_logins.xlsx")

print("Mean of number_of_login: ", df["number_of_login"].mean())
print("Std of number_of_login: ", df["number_of_login"].std())
