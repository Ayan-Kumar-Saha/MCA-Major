from utils import is_valid_path, wait
import os
import requests

local_data_directory_path = 'datasets'

leukemia_remote_URL = 'https://raw.githubusercontent.com/kalyaniuniversity/mgx-datasets/master/leukemia/datasets/preprocessed/'

dlbcl_remote_URL = 'https://raw.githubusercontent.com/kalyaniuniversity/mgx-datasets/master/DLBCL/datasets/preprocessed/'

childall_remote_URL = 'https://raw.githubusercontent.com/kalyaniuniversity/mgx-datasets/master/GSE412/datasets/preprocessed/'

mll_leukemia_remote_URL = 'https://raw.githubusercontent.com/kalyaniuniversity/mgx-datasets/master/MLL/datasets/preprocessed/'


def isin_local_data_directory(file_name):

    global local_data_directory_path

    print('\nSearching data locally...')

    complete_file_path = os.path.join(local_data_directory_path, file_name)

    if is_valid_path(local_data_directory_path):

        if is_valid_path(complete_file_path):

            print('FOUND!!')
            return True

    print('NOT FOUND!!')
    return False

    
def store_in_local_data_directory(remote_URL, dataset_name):

    global local_data_directory_path

    local_data_path = os.path.join(local_data_directory_path, dataset_name)

    if not is_valid_path(local_data_directory_path):
        os.mkdir(local_data_directory_path)

    try:
        print(f'\nLoading {dataset_name} from a Remote URL...')

        resp = requests.get(remote_URL)

        csv_file = open(local_data_path, 'wb')

        print(f'\n\nMaking a local copy of the {dataset_name} for future use...')

        csv_file.write(resp.content)

        print(f'\n\nLocal copy of {dataset_name} saved successfully!!')
    
    except:
        print(f'\n\nSome error occured while loading {dataset_name} from Remote URL...status code {resp.status_code}!!')
    

def provide_leukemia_dataset(choice):

    global leukemia_remote_URL

    if choice == 1:
        dataset_name = 'leukemia-selected-10-snr.csv'
    
    elif choice == 2:
        dataset_name = 'leukemia-selected-25-snr.csv'

    elif choice == 3:
        dataset_name = 'leukemia-selected-100-snr.csv'
    
    else:
        dataset_name = 'leukemia-selected-1000-snr.csv'

    remote_URL = leukemia_remote_URL + dataset_name

    if not isin_local_data_directory(dataset_name):

        store_in_local_data_directory(remote_URL, dataset_name)

    return dataset_name


def provide_dlbcl_dataset(choice):

    global dlbcl_remote_URL

    if choice == 5:
        dataset_name = 'dlbcl-selected-10-snr.csv'
    
    elif choice == 6:
        dataset_name = 'dlbcl-selected-25-snr.csv'

    elif choice == 7:
        dataset_name = 'dlbcl-selected-100-snr.csv'

    else:
        dataset_name = 'dlbcl-selected-1000-snr.csv'

    remote_URL = dlbcl_remote_URL + dataset_name

    if not isin_local_data_directory(dataset_name):

        store_in_local_data_directory(remote_URL, dataset_name)
    
    return dataset_name


def provide_child_all_dataset(choice):

    global childall_remote_URL

    if choice == 9:
        dataset_name = 'child-all-selected-10-snr.csv'
    
    elif choice == 10:
        dataset_name = 'child-all-selected-25-snr.csv'

    elif choice == 11:
        dataset_name = 'child-all-selected-100-snr.csv'

    else:
        dataset_name = 'child-all-selected-1000-snr.csv'

    remote_URL = childall_remote_URL + dataset_name

    if not isin_local_data_directory(dataset_name):

        store_in_local_data_directory(remote_URL, dataset_name)

    return dataset_name


def provide_mll_leukemia_dataset(choice):

    global mll_leukemia_remote_URL

    if choice == 13:
        dataset_name = 'mll-leukemia-selected-10.csv'
    
    elif choice == 14:
        dataset_name = 'mll-leukemia-selected-25.csv'

    elif choice == 15:
        dataset_name = 'mll-leukemia-selected-100.csv'

    else:
        dataset_name = 'mll-leukemia-selected-1000.csv'

    remote_URL = mll_leukemia_remote_URL + dataset_name

    if not isin_local_data_directory(dataset_name):

        store_in_local_data_directory(remote_URL, dataset_name)

    return dataset_name


def get_predefined_dataset():

    while True:
        print('\nPlease a choose a dataset')
        print('1. Leukemia dataset with 10 attributes')
        print('2. Leukemia dataset with 25 attributes')
        print('3. Leukemia dataset with 100 attributes')
        print('4. Leukemia dataset with 1000 attributes')
        print('5. DLBCL dataset with 10 attributes')
        print('6. DLBCL dataset with 25 attributes')
        print('7. DLBCL dataset with 100 attributes')
        print('8. DLBCL dataset with 1000 attributes')
        print('9. Child All dataset with 10 attributes')
        print('10. Child All dataset with 25 attributes')
        print('11. Child All dataset with 100 attributes')
        print('12. Child All dataset with 1000 attributes')
        print('13. MLL Leukemia dataset with 10 attributes')
        print('14. MLL Leukemia dataset with 25 attributes')
        print('15. MLL Leukemia dataset with 100 attributes')
        print('16. MLL Leukemia dataset with 1000 attributes')

        choice = int(input('\nEnter your choice: '))

        if choice in [1, 2, 3, 4]:
            return provide_leukemia_dataset(choice)
        
        elif choice in [5, 6, 7, 8]:
            return provide_dlbcl_dataset(choice)

        elif choice in [9, 10, 11, 12]:
            return provide_child_all_dataset(choice)
        
        elif choice in [13, 14, 15, 16]:
            return provide_mll_leukemia_dataset(choice)
        
        else:
            print('\nWrong Input! Enter again!')