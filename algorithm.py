import pandas as pd
from clustering_implementation import implement_kmeans, implement_agglomerative, implement_spectral, implement_birch, implement_all
from data_manager import get_predefined_dataset
from output_manager import write_to_csv, display_clustering_result
from utils import is_valid_path, extract_filename
import os
import time

user_dataset_flag = False
dataset_path = None
dataset_name = None
user_dataset_class_attribute = None
local_data_directory_path = 'datasets'

switcher = {
        1: implement_kmeans,
        2: implement_spectral,
        3: implement_agglomerative,
        4: implement_birch,
        5: implement_all,
    }


def get_dataset_choice():

    global dataset_name
    global user_dataset_flag

    print('\n1. Use default datasets')
    print('2. Use own datasets')

    response = int(input('\nEnter your choice: '))

    if response == 2:
        dataset_name = get_dataset_from_user()
        user_dataset = True

    else:
        dataset_name = get_predefined_dataset()


def get_dataset_from_user():

    global dataset_path
    global user_dataset_class_attribute

    while True:

        dataset_path = input('\nPlease provide the path of the dataset: ')

        if is_valid_path(dataset_path):
            user_dataset_class_attribute = input('\nPlease provide the class label attribute name: ')
            return extract_filename(dataset_path)
        
        print("\nPath doesn't exist! Please provide a valid path!")


def get_dataset_as_dataframe():

    global dataset_path
    global dataset_name
    global local_data_directory_path

    if user_dataset_flag:
        path = dataset_path
    
    else:
        path = os.path.join(local_data_directory_path, dataset_name)

    return pd.read_csv(path)


def switch(choice, df):

    global switcher
    # global dataset_name

    if user_dataset_flag:
        return switcher.get(choice)(df.copy(), class_attribute = user_dataset_class_attribute)

    else:
        return switcher.get(choice)(df.copy(), class_attribute= 'class')

def main():

    global dataset_name

    get_dataset_choice()

    while True:

        df = get_dataset_as_dataframe()
        
        print('\n\n--MAIN MENU--')
        print('1. KMeans')
        print('2. Spectral Clustering')
        print('3. Agglomerative Clustering')
        print('4. Birch')
        print('5. Run ALL')
        print('6. Run ALL and Generate Report')
        print('0: EXIT')

        choice = int(input('\nEnter your choice: '))

        if choice not in range(7):
            print('Invalid choice!! Enter again!!')

        elif choice == 0:
            break

        else:

            if choice == 6:
                result = switch(5, df)
                write_to_csv(dataset_name, result)

            else:
                result = switch(choice, df)

            display_clustering_result(result)


main()