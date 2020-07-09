import numpy as np 
import pandas as pd
import os

def get_file_list(path):

    return os.listdir(path)


def get_dataframe(path):

    return pd.read_csv(path, index_col=0, header=0)


def get_ranked_data(df):

    for val in df.columns: 
        a = {}
        rank = 1
        for num in sorted(df[val], reverse = True):
            if num not in a:
                a[num] = rank
                rank = rank+1

        df[val] = [a[i] for i in df[val]]



def main():

    if not os.path.exists('output/ranked_reports'):
        os.mkdir('output/ranked_reports')

    report_files_list = get_file_list('output/reports')

    for file in report_files_list:

        name = file.split('.')[0]

        df = get_dataframe(os.path.join('output/reports', file))

        get_ranked_data(df)

        df.to_csv(f'output/ranked_reports/{name}.csv')

    print("Check 'output/ranked_reports directory' for all the ranked report files!")

main()


