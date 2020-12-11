# CNA 330 Group Project fuel prices throughout the years. How the pandemic has affected gas prices#
# Collaborated with Eric, Dillion, Igor, Vlado, Mohammad,
# Help from Justin Ellis & Zac Rubin #
# 12/9/2020 #
# This script pulls from the eia website and stores fuel prices into a database. It takes the information and compiles into a xcel sheet.
# CNA 330 Group Project - Michael Horton, Carlos

from sqlalchemy import create_engine # https://www.geeksforgeeks.org/how-to-convert-pandas-dataframe-into-sql-in-python/
import pandas as pd
from matplotlib import pyplot as plt

hostname="127.0.0.1"
uname="root"
pwd=""
dbname="sql-group-project"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host="127.0.0.1", db=sql-group-project, user=root, pw=""))

df = pd.read_sql_table('Fuel', engine)

print(df)

plt.figure(figsize=(24, 24))
plt.plot(df['Date'], df['Diesel_Price'])
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Diesel Price')
plt.title('Diesel Over Time', fontsize=16)
plt.show()
