import os
import pandas as pd
import numpy as np




def loop_dir(directory):
    fp = directory + '/data'
    data = os.listdir(fp)
    exp_num = 0
    out_df = pd.DataFrame(columns=['X', 'Y', 'Z', 'alpha', 'gamma', 'beta', 'activity','test', 'exp_num'])
    for file_ in data:
        if 'txt' in file_:
            b = pd.read_csv(fp+f'/{file_}')
            b.columns = ['X', 'Y', 'Z', 'alpha', 'gamma', 'beta', 'activity','test']
            b['exp_num'] = exp_num
            out_df = pd.concat([out_df, b])
            exp_num += 1
    return out_df



if __name__ == '__main__':
    root = '/home/devin/Documents/Galvanize/repos/'
    repo = 'Raspberry-Pi-Human-Act-Rec'
    directory = root + repo
    out_df = loop_dir(directory)
    out_df.to_csv('data/merged_data.txt')
    