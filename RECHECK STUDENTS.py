import datetime
import time
from pathlib import Path
import ntpath
from IPython.display import display
import pandas as pd
SUB_LIST = ['AI', 'HCI', 'SC&D', 'CCN', 'EE']

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
path = Path("F:/ADNAN/FACE RECOGNIATION SYSTEM/Attendance/HIII-2023-01-08/")
csvlist = path.glob("*.csv")
pd_csv_dict = {}
"""for csv_file in csvlist:
    file_name = ntpath.basename(csv_file)
    pd_csv_dict['pd_' + file_name] = pd.read_csv(csv_file, sep=";", encoding='mac_roman')
locals().update(pd_csv_dict)
print(pd_csv_dict)"""
csvs = [pd.concat(pd.read_csv(g, header=None, skiprows=1) for g in csvlist)]
print(csvs)
"""for f in csvlist:
    # read the csv file
    df = pd.read_csv(f, header=None, skiprows=1)
    dataframes_list.append(df)
    # print the location and filename
    # print('Location:', f)
    # print('File Name:', f.split("/")[-1])

    # print the content
    # print('Content:')
for dataset in dataframes_list:
    display(dataset)"""

# display(df)

"""paths, dirs, files = next(csvlist())
file_count = len(files)
# create empty list
dataframes_list = []

# append datasets to the list
for i in range(file_count):
    temp_df = pd.read_csv("./csv/" + files[i])
    dataframes_list.append(temp_df)

# display datasets
for dataset in dataframes_list:
    display(dataset)"""

"""# to iterate csv file one by one
# inside the folder
for file in csvlist:
    # combining multiple excel worksheets
    # into single data frames
    df = pd.concat(pd.read_csv(file))

    # appending csv files one by one
    finalcsvsheet = finalcsvsheet.append(df, ignore_index=True)

# to print the combined data
print('Final Sheet:')
display(finalcsvsheet)"""