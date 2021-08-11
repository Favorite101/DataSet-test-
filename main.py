import pandas as pd
import numpy as np
df = pd.read_csv('bp_loan_task_log.csv', delimiter=";")
sort_df = df.sort_values(by='time')
cols = ['kindName', 'otherKindName', 'count', 'count_unique', 'min_time', 'max_time', 'avg_time']
df2 = pd.DataFrame(columns=cols, index=range(6878))
for k in range(0, 6878):
    count_df = sort_df.loc[k].kind + sort_df.loc[k+1].kind
    uniq_id = sort_df.loc[k].task
    min_time = sort_df.loc[k].time.min()
    max_time = sort_df.loc[k].time.max()
    avg_time = sort_df.loc[k].time.mean()
    df2.loc[k].kindName = sort_df.loc[k].kindName
    df2.loc[k].otherKindName = sort_df.loc[k+1].kindName
    df2.loc[k].count = count_df
    df2.loc[k].count_unique = uniq_id
    df2.loc[k].min_time = min_time
    df2.loc[k].max_time = max_time
    df2.loc[k].avg_time = avg_time
    print(sort_df.loc[k].kindName, sort_df.loc[k+1].kindName, count_df, uniq_id, min_time, max_time, avg_time)
df2.to_csv('DataSet.csv', index=False, sep=";")