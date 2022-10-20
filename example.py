from pandas_sqlite3.pandas_query import pandas_query
import pandas as pd


sample_df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

long_petal_df = sample_df.loc[sample_df['petal_length'] > 5].copy()

sql_query = """
                SELECT 
                        S.*
                FROM sample_df s
                JOIN long_petal_df USING ('sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species')
            """

final_df = pandas_query(dfs=[sample_df, long_petal_df], df_names=['sample_df', 'long_petal_df'], sql=sql_query)

