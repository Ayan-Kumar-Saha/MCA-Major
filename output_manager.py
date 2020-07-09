import csv
import os

def display_clustering_result(result):

    for key in result:
        print(f'Completeness score: {result[key]["cs"]}')
        print(f'Homogeneity score: {result[key]["hs"]}')
        print(f'FMI index: {result[key]["fmi"]}')
        print(f'Normalized mutual info score: {result[key]["nmis"]}')
        print(f'Confusion Matrix: \n{result[key]["con"]}')
    

def write_to_csv(dataset_name, report):

    dataset = dataset_name.split('.')[0]

    print("\n\nResult is stored in the directory: 'output'")
    print("-------------------------------------------")

    if not os.path.exists('output'):
        os.mkdir('output')

    if not os.path.exists('output/confusion_matrices'):
            os.mkdir('output/confusion_matrices')

    if not os.path.exists('output/reports'):
            os.mkdir('output/reports')

    for key in report:

        with open(f'output/confusion_matrices/{dataset}-{key}.csv', 'w') as confusion_matrix_file:

            confusion_matrix = report[key]['con']

            csv_writer = csv.writer(confusion_matrix_file)

            for row in confusion_matrix:

                csv_writer.writerow(row)

    print("\nConfusion matrices have been stored in the directory: output/confusion_matrices")


    # file_exists = False

    # if os.path.exists(f"output/{dataset}-report.csv"):
    #     file_exists = True

    with open(f"output/reports/{dataset}-report.csv", 'w') as csvfile:

        csv_writer = csv.writer(csvfile)
        # accuracy_score = list()

        for key in report:

          confusion_matrix = report[key]['con']

          digonal_sum = sum(confusion_matrix.diagonal())

          total_sum = confusion_matrix.sum()
          
        #   accuracy_score.append(digonal_sum/total_sum)
          report[key]['acc'] = (digonal_sum/total_sum)

        csv_writer.writerow(['clustering_index', 'completeness_score', 'homogeneity_score', 'fowlkes_mallows_score', 'normalized_mutual_info_score', 'accuracy'])

        for key in report:

            new_row = list()

            new_row.append(key)

            new_row.append(report[key]['cs'])
            new_row.append(report[key]['hs'])
            new_row.append(report[key]['fmi'])
            new_row.append(report[key]['nmis'])
            new_row.append(report[key]['acc'])

            csv_writer.writerow(new_row)
  
        # completeness_score = [report[key]['cs'] for key in report]
        # # completeness_score.insert(0, dataset_name)
        # completeness_score.insert(0, 'completeness score')

        # homogeneity_score = [report[key]['hs'] for key in report]
        # # homogeneity_score.insert(0, dataset_name)
        # homogeneity_score.insert(0, 'homogeneity score')

        # fowlkes_mallows_score = [report[key]['fmi'] for key in report]
        # # fowlkes_mallows_score.insert(0, dataset_name)
        # fowlkes_mallows_score.insert(0, 'fowlkes mallows score')

        # normalized_mutual_info_score = [report[key]['nmis'] for key in report]
        # # normalized_mutual_info_score.insert(0, dataset_name)
        # normalized_mutual_info_score.insert(0, 'normalized mutual info score')

        # # accuracy_score.insert(0, dataset_name)
        # accuracy_score.insert(0, 'accuracy score')

        # # if not file_exists:

        

        # csv_writer.writerow(completeness_score)
        # csv_writer.writerow(homogeneity_score)
        # csv_writer.writerow(fowlkes_mallows_score)
        # csv_writer.writerow(normalized_mutual_info_score)
        # csv_writer.writerow(accuracy_score)

    print("\nClustering results has been stored in the file: output/report.csv")