
from datetime import datetime
from database import fetch_users

print(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

df_manager = fetch_users("damerchi")
print(df_manager)