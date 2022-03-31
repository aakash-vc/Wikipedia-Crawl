import pandas as pd


class Process:

    def __init__(self):
        pass

    def get_connections(self, lst):
        res = []
        for i in range(len(lst)-1):
            res.append([lst[i].split('/')[-1].replace('_', " "), lst[i+1].split('/')[-1].replace('_', " ")])

        df =  pd.DataFrame(res, columns=['From', 'To'])
        return df

    def merge_dataframes(self, df):
        old_df = pd.read_csv('data/connections.csv')
        new_df = pd.concat([old_df, df])

        df = new_df.drop_duplicates(subset=['From', 'To'], keep='last')
        #df = df.sort_values(by='From', ignore_index=True)

        return df