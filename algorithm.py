import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, AffinityPropagation, MeanShift, SpectralClustering, AgglomerativeClustering, DBSCAN, OPTICS, Birch
from utils import calculate_clustering_accuracy, display_clustering_accuracy, write_to_csv


dataset_name = None
dataset = None
data = None
actual_labels = None

report = dict()


def prepare_dataset():

    global dataset
    global data
    global actual_labels

    df = pd.read_csv('datasets/leukemia-preprocessed-datasets/leukemia-selected-10.csv')

    df['class'] = df['class'].apply(lambda x: 0 if x == 'ALL' else 1)

    data = df.drop('class',axis=1).copy()

    actual_labels = df['class']


def implement_KMeans(clustering_data):

    model = KMeans(n_clusters=2, random_state=1)

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- KMeans Clustering -----\n')

    report['kmeans'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['kmeans'])


def implement_Affinity_Propagation(clustering_data):

    model = AffinityPropagation()

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- Affinity Propagation Clustering -----\n')

    report['affinity_propagation'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['affinity_propagation'])


def implement_MeanShift(clustering_data):

    model = MeanShift()

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- MeanShift Clustering -----\n')

    report['meanshift'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['meanshift'])


def implement_Spectral_Clustering(clustering_data):

    model = SpectralClustering(n_clusters=2, random_state=0)

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- Spectral Clustering -----\n', end='\n')

    report['spectral'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['spectral'])


def implement_Agglomerative_Clustering(clustering_data):

    model = AgglomerativeClustering(n_clusters=2)

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- Agglomerative Clustering -----\n', end='\n')

    report['agglomerative'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['agglomerative'])


def implement_DBSCAN(clustering_data):

    model = DBSCAN()

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- DBSCAN Clustering -----\n')

    report['dbscan'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['dbscan'])


def implement_OPTICS(clustering_data):

    model = OPTICS()

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- OPTICS Clustering -----\n')

    report['optics'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['optics'])


def implement_Birch(clustering_data):

    model = Birch(n_clusters=2)

    predicted_labels = model.fit_predict(clustering_data)

    print('\n----- Birch Clustering -----\n')

    report['birch'] = calculate_clustering_accuracy(actual_labels, predicted_labels)

    display_clustering_accuracy(report['birch'])


def implement_ALL(clustering_data):

    implement_KMeans(clustering_data)
    implement_Affinity_Propagation(clustering_data)
    implement_MeanShift(clustering_data)
    implement_Spectral_Clustering(clustering_data)
    implement_Agglomerative_Clustering(clustering_data)
    implement_DBSCAN(clustering_data)
    implement_OPTICS(clustering_data)
    implement_Birch(clustering_data)


def generate_report():

    global dataset_name
    global report

    dataset_name = input('Enter a name for the dataset: ')

    implement_ALL(data.copy())
    write_to_csv(dataset_name, report)


switcher = {
        1: implement_KMeans,
        2: implement_Affinity_Propagation,
        3: implement_MeanShift,
        4: implement_Spectral_Clustering,
        5: implement_Agglomerative_Clustering,
        6: implement_DBSCAN,
        7: implement_OPTICS,
        8: implement_Birch,
        9: implement_ALL,
        10: generate_report
    }


def switch(choice):

    global switcher

    if choice == 10:
      return switcher.get(choice)()
    else:
      return switcher.get(choice)(data.copy())


def main():

    prepare_dataset()

    while True:
        print('\n\n--MAIN MENU--')
        print('1. KMeans')
        print('2. Affinity Propagation')
        print('3. MeanShift')
        print('4. Spectral Clustering')
        print('5. Agglomerative Clustering')
        print('6. DBSCAN')
        print('7. OPTICS')
        print('8. Birch')
        print('9. Run ALL')
        print('10. Run ALL and Generate Report')
        print('0: EXIT')

        choice = int(input('\nEnter your choice: '))

        if choice not in range(11):
            print('Invalid choice')

        elif choice == 0:
            break

        else:
            switch(choice)


main()
