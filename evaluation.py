from sklearn.metrics import completeness_score, homogeneity_score, fowlkes_mallows_score, normalized_mutual_info_score, confusion_matrix, classification_report

import numpy as np

from mapping import get_mapped_actual_class_labels

def get_clustering_accuracy(actual, predicted):

    cs = completeness_score(actual, predicted)
    hs = homogeneity_score(actual, predicted)
    fmi = fowlkes_mallows_score(actual, predicted)
    nmis = normalized_mutual_info_score(actual, predicted)
    con = confusion_matrix(actual, predicted)
    print(f'Classification Report: \n', classification_report(actual, predicted))
    return {
        'cs': cs, 'hs': hs, 'fmi': fmi, 'nmis': nmis, 'con': con
    }


def get_actual_labels_count(df, class_attribute):

    return df[class_attribute].value_counts()


def evaluate_clustering(df, class_attribute, predicted_labels):

    actual_labels_count = get_actual_labels_count(df, class_attribute)

    mapped_actual_class_labels = get_mapped_actual_class_labels(df, class_attribute, actual_labels_count, predicted_labels)

    # print('preicted: ',predicted_labels)
    # print('actual: ',np.array(mapped_actual_class_labels))

    result = get_clustering_accuracy(mapped_actual_class_labels, predicted_labels)

    # print(result)

    return result