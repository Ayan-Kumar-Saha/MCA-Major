from sklearn.metrics import completeness_score, homogeneity_score, fowlkes_mallows_score, normalized_mutual_info_score, confusion_matrix, classification_report
import csv
import os


def calculate_clustering_accuracy(actual, predicted):

    cs = completeness_score(actual, predicted)
    hs = homogeneity_score(actual, predicted)
    fmi = fowlkes_mallows_score(actual, predicted)
    nmis = normalized_mutual_info_score(actual, predicted)
    con = confusion_matrix(actual, predicted)
    print(f'Classification Report: \n', classification_report(actual, predicted))
    return {
        'cs': cs, 'hs': hs, 'fmi': fmi, 'nmis': nmis, 'con':con
    }


def display_clustering_accuracy(report):

    print(f'Completeness score: {report["cs"]}')
    print(f'Homogeneity score: {report["hs"]}')
    print(f'FMI index: {report["fmi"]}')
    print(f'Normalized mutual info score: {report["nmis"]}')
    print(f'Confution Matrix: \n{report["con"]}')
    

def write_to_csv(dataset_name, report):

    print("\n\nResult is stored in the directory: 'output'")
    print("-------------------------------------------")

    if not os.path.exists('output'):
        os.mkdir('output')

    if not os.path.exists('output/confusion_matrices'):
            os.mkdir('output/confusion_matrices')

    for key in report:

        with open(f'output/confusion_matrices/{dataset_name}-{key}.csv', 'w') as confusion_matrix_file:

            confusion_matrix = report[key]['con']

            csv_writer = csv.writer(confusion_matrix_file)

            for row in confusion_matrix:

                csv_writer.writerow(row)

    print("\nConfusion matrices have been stored in the directory: output/confusion_matrices")


    file_exists = False

    if os.path.exists('output/report.csv'):
        file_exists = True

    with open('output/report.csv', 'a') as csvfile:

        csv_writer = csv.writer(csvfile)
        accuracy_score = list()

        for key in report:

          confusion_matrix = report[key]['con']

          digonal_sum = sum(confusion_matrix.diagonal())

          total_sum = confusion_matrix.sum()
          
          accuracy_score.append(digonal_sum/total_sum)
  
        completeness_score = [report[key]['cs'] for key in report]
        completeness_score.insert(0, dataset_name)
        completeness_score.insert(1, 'completeness score')

        homogeneity_score = [report[key]['hs'] for key in report]
        homogeneity_score.insert(0, dataset_name)
        homogeneity_score.insert(1, 'homogeneity score')

        fowlkes_mallows_score = [report[key]['fmi'] for key in report]
        fowlkes_mallows_score.insert(0, dataset_name)
        fowlkes_mallows_score.insert(1, 'fowlkes mallows score')

        normalized_mutual_info_score = [report[key]['nmis'] for key in report]
        normalized_mutual_info_score.insert(0, dataset_name)
        normalized_mutual_info_score.insert(1, 'normalized mutual info score')

        accuracy_score.insert(0, dataset_name)
        accuracy_score.insert(1, 'accuracy score')

        if not file_exists:

            csv_writer.writerow(['dataset_name', 'clustering index', 'KMeans', 'Affinity Propagation', 'MeanShift', 'Spectral', 'Agglomerative', 'DBSCAN', 'OPTICS', 'Birch'])

        csv_writer.writerow(completeness_score)
        csv_writer.writerow(homogeneity_score)
        csv_writer.writerow(fowlkes_mallows_score)
        csv_writer.writerow(normalized_mutual_info_score)
        csv_writer.writerow(accuracy_score)

    print("\nClustering results has been stored in the file: output/report.csv")



