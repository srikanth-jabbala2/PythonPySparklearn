from config.db_config import connect_sql_server

import pandas as pd

def load_target_data(query):
    conn = connect_sql_server()
    return pd.read_sql(query, conn)