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
    plt.plot(df['DATE'], df['T1'], c='black', ls='-', lw=1, label='$T_1$')
    plt.plot(df['DATE'], df['T2'], 'r-', lw=0.5, label='$T_2$')
    plt.plot(df['DATE'], df['T3'], 'g-', lw=0.5, label='$T_3$')
    plt.plot(df['DATE'], df['T4'], 'b-', lw=0.5, label='$T_4$')
    plt.plot(df['DATE'], df['MODE'] * df.max().values[1:].max(), 'c-', label='MODE')
    plt.xlabel('Time')
    plt.ylim((-30, 40))
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
