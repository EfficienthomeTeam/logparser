import numpy as np
import pandas as pd
import re
import os
from os.path import join as jp

from tqdm import tqdm

from warnings import warn
import logging 

# add filemode="w" to overwrite
logging.basicConfig(filename="%s.log" % str(pd.datetime.now()).split()[0], filemode='w', level=logging.INFO)
 
def log_to_dataframe(fp):
    """
    Function to convert input log file into `pd.DataFrame`
    _ _ _ _ _ _ 
    Parameters:
    `fp` - filepath, str
    
    _ _ _ _ _ _ 
    Output:
    `df` - converted dataframe, `pd.DataFrame`
    """
    dates = []
    list_temperatures = []
    modes = []
    with open(fp, "r") as f:
        for i, line in tqdm(enumerate(f)):
            str_date, str_array = line.split(': ')
            date = pd.datetime.strptime(str_date, "%Y-%m-%dT%H:%M:%S.%fZ")
            dates.append(date)

            temperatures = []
            val_list = re.sub('[\[\]\,"]', '', str_array).split()
            for val in val_list:
                try:
                    temp = float(val)
                    temperatures.append(temp)
                except ValueError as e:
                    if val == 'on' or val == 'off':
                        modes.append(val)
                    else:
                        warn("Unrecognised value `%s` in %s line of file `%s` " % (val, i+1, fp))
                        logging.warning("Unrecognised value `%s` in %s line of file `%s` " % (val, i+1, fp))
                        modes.append(np.nan)
            if len(temperatures) != 4:
                warn("Possibly missing value in %s line of file `%s` " % (i+1, fp))
                logging.warning("Possibly missing value in %s line of file `%s` " % (i+1, fp))
            list_temperatures.append(temperatures)
    df = pd.DataFrame(data=list_temperatures, columns=['T_1', 'T_2', 'T_3', 'T_4'])
    df['DATE'] = dates
    df['MODE'] = modes
    
    return df[['DATE', 'T_1', 'T_2', 'T_3', 'T_4', 'MODE']]


def convert_folder(log_dir):
    """
    Function to convert folder with log files into one `pd.DataFrame`
    _ _ _ _ _ _ 
    Parameters:
    `log_dir` - path to the directory with log files extracted, str
   
    _ _ _ _ _ _ 
    Output:
    `data` - converted dataframe, `pd.DataFrame`
    
    _ _ _ _ _ _
    Note: check the `*.log` file with possibly incorrected files
    
    """
    for ix, file_path in tqdm(enumerate(os.listdir(log_dir))):
        df = log_to_dataframe(jp(log_dir, file_path))
        if ix == 0:
            data = df
        else:
            data = pd.concat([data, df], axis=0, ignore_index=True)

    return data


if __name__ == '__main__':
    df = log_to_dataframe('./log_dir/data-2018-12-14-21.log')
    print('Done!')