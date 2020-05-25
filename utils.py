from sklearn.metrics import completeness_score, homogeneity_score, fowlkes_mallows_score, normalized_mutual_info_score
import csv
import os


def calculate_clustering_accuracy(actual, predicted):

    cs = completeness_score(actual, predicted)
    hs = homogeneity_score(actual, predicted)
    fmi = fowlkes_mallows_score(actual, predicted)
    nmis = normalized_mutual_info_score(actual, predicted)

    return {
        'cs': cs, 'hs': hs, 'fmi': fmi, 'nmis': nmis
    }


def display_clustering_accuracy(report):

    print(f'Completeness score: {report["cs"]}')
    print(f'Homogeneity score: {report["hs"]}')
    print(f'FMI index: {report["fmi"]}')
    print(f'Normalized mutual info score: {report["nmis"]}')


def write_to_csv(dataset_name, report):

    file_exists = False

    if os.path.exists('report.csv'):
        file_exists = True

    with open('report.csv', 'a') as csvfile:

        csv_writer = csv.writer(csvfile)

        completeness_score = [report[key]['cs'] for key in report]
        completeness_score.insert(0, dataset_name)

        homogeneity_score = [report[key]['hs'] for key in report]
        homogeneity_score.insert(0, dataset_name)

        fowlkes_mallows_score = [report[key]['fmi'] for key in report]
        fowlkes_mallows_score.insert(0, dataset_name)

        normalized_mutual_info_score = [report[key]['nmis'] for key in report]
        normalized_mutual_info_score.insert(0, dataset_name)

        if not file_exists:

            csv_writer.writerow(['dataset_name', 'KMeans', 'Affinity Propagation', 'MeanShift', 'Spectral', 'Agglomerative', 'DBSCAN', 'OPTICS', 'Birch'])

        csv_writer.writerow(completeness_score)
        csv_writer.writerow(homogeneity_score)
        csv_writer.writerow(fowlkes_mallows_score)
        csv_writer.writerow(normalized_mutual_info_score)

    print("Report is generated!! Check 'report.csv'!")




