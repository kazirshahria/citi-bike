import os
from datetime import datetime
import pandas as pd

path = os.getcwd()
data_path = os.path.join(path, 'data')
data_files = os.listdir(data_path)

dfs = []
for i, data_file in enumerate(data_files, start=1):
    if data_file != 'zip':
        trip_data_path = os.path.join(data_path, data_file)
        csv_files = os.listdir(trip_data_path)
        for csv_file in csv_files:
            csv_path = os.path.join(trip_data_path, csv_file)
            dfs.append(pd.read_csv(csv_path, dtype='str'))
    print(f'[{datetime.now().strftime('%d/%m/%Y %H:%M')}]: {i}/{len(data_files)}')

save_path = os.path.join(data_path, '2025-citibike.csv')
df = pd.concat(dfs)
df.to_csv(save_path)
