import os
import time

def show_status_wait(message, waiting_time):
    """ Displays a message to sys.stdout and delays the program execution for a given time.

    Args:
        message (string): a message that will be displayed
        waiting_time (float): time to delay program execution in seconds
    """

    print(message, end='')
    time.sleep(waiting_time)


def wait(waiting_time):
    """ Delays the program execution for a given time.

    Args:
        waiting_time (float): time to delay program execution in seconds
    """

    time.sleep(waiting_time)

def is_valid_path(path):
    """ Checks if a path is valid or not.

    Args:
        path (string): complete path of a file

    Returns:
        boolean: True if the path is valid otherwise False
    """
    
    if os.path.exists(path):
        return True

    else:
        return False


def extract_filename(path):
    """ Returns the filename from a path.

    Args:
        path (string): complete path of a file

    Returns:
        string: filename
    """

    return path.split('/')[-1]


def extract_clustering_data(df, class_attribute):

    return df.drop(class_attribute, axis = 1).copy()


