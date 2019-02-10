import numpy as np
import pandas as pd

import pickle
import json

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def plot_ts(df):
    plt.figure(figsize=(18,10))
    plt.title('Timeseries plot')
    plt.plot(df['DATE'], df['EXT_T'], c='black', ls='-', lw=1, label='$EXT_T$')
    plt.plot(df['DATE'], df['TOP_T'], 'r-', lw=0.5, label='$TOP_T$')
    plt.plot(df['DATE'], df['MIDDLE_T'], 'g-', lw=0.5, label='$MIDDLE_T$')
    # plt.plot(df['DATE'], df['ENERGY_PULSES'], 'b-', lw=0.5, label='$ENERGY_PULSES$')
    plt.plot(df['DATE'], df['HEATER'] * 65, 'c-', label='HEATER')
    plt.xlabel('Time')
    plt.ylim((-30, 65))
    plt.legend(loc='best')
    plt.show()


def log_str(string, fp):
    with open(fp, 'w') as f:
        f.write(string)

        
def log_json(params, fp):
    with open(fp, 'w') as f:
        json.dump(params, f)
    
    
def save(model, path):
    pickle.dump(model, open(path, 'wb'))
    
    
def load(path):
    return pickle.load(open(path,'rb'))
