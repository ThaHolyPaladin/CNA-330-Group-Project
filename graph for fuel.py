# CNA 330 Group Project fuel prices throughout the years. How the pandemic has affected gas prices#
# Collaborated with Eric, Dillion, Igor, Vlado, Mohammad,
# Help from Justin Ellis & Zac Rubin #
# 12/9/2020 #
# This script pulls from the eia website and stores fuel prices into a database. It takes the information and compiles into a xcel sheet.
# CNA 330 Group Project - Michael Horton, Carlos

from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

hostname="127.0.0.1"
uname="root"
pwd="root"
dbname="sql-group-project"
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

df = pd.read_sql_table('fuel', engine)

print(df)

plt.figure(figsize=(24, 24))
plt.plot(df['Date'], df['Price'])
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Fuel Price')
plt.title('Fuel Over Time', fontsize=16)
plt.show()
