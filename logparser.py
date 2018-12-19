import numpy as np
import pandas as pd
import re
from warnings import warn

from tqdm import tqdm


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
                        warn("Unrecognised value `%s` in %s line of file" % (val, i+1))
                        modes.append(np.nan)
            if len(temperatures) != 4:
                warn("Possibly missing value in %s line of file" % (i+1))
            list_temperatures.append(temperatures)
    df = pd.DataFrame(data=list_temperatures, columns=['T_1', 'T_2', 'T_3', 'T_4'])
    df['DATE'] = dates
    df['MODE'] = modes
    
    return df[['DATE', 'T_1', 'T_2', 'T_3', 'T_4', 'MODE']]


if __name__ == '__main__':
    df = log_to_dataframe('./log_dir/data-2018-12-18-09.log')
    print('Done!')