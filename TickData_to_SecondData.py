import csv, os
import pandas as pd
from datetime import datetime
import glob

os.chdir(r"path/to/file")
for subdir, dirs, files in os.walk(r"path/to/file"):
    for file in files:
        newpath = os.path.join(subdir, file)
        if newpath.endswith(".csv"):
            with open(newpath, 'rb') as i:
                try:
                    data_frame = pd.read_csv(i, header=None)
                    time1 = data_frame.iloc[:,0]/1000
                    hour = time1 // 3600
                    time1 %= 3600
                    minutes = time1 // 60
                    time1 %= 60
                    seconds = time1
                    trade_time_df = hour.map(str) + minutes.map(str) + seconds.map(str)
                    current_day = newpath.split(os.sep)[6]
                    current_day_trade_time = current_day + trade_time_df
                    #date_1 = current_day_trade_time.apply(lambda x: datetime.strptime(x, '%Y%m%d%H.0%M.0%S.%f'))
                    date_1 = pd.to_datetime(current_day_trade_time, format='%Y%m%d%H.0%M.0%S.%f', errors='coerce')
                    date_2 = date_1.dropna()
                    date_3 = date_2.apply(lambda x:x.strftime('%Y%m%d %H:%M:%S'))
                    date_3 = pd.to_datetime(date_3)
                    data_frame.iloc[:,0] = date_3
                    data_frame.index = data_frame.iloc[:,0]
                    data_frame.index.name = None
                    current_file = newpath.split(os.sep)[7]
                    ofile = r"pathtofile"
                    if not os.path.isdir(ofile):
                            os.mkdir(ofile)
                    newpath4 = os.path.join(ofile, current_day)
                    newpath4 = os.path.join(newpath4, '')
                    if not os.path.isdir(newpath4):
                            os.makedirs(newpath4)
                    os.chdir(r"path to file")
                    data_frame.to_csv(newpath4 + "\\" + current_file)
                except:
                    pass
                i.close()
                os.chdir(r"pathtofile")
