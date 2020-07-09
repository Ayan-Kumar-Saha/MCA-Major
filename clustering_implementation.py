from sklearn.cluster import KMeans, AgglomerativeClustering, SpectralClustering, Birch
from evaluation import evaluate_clustering
# from algorithm import user_dataset_flag, user_dataset_class_attribute
from utils import extract_clustering_data


def implement_kmeans(df, class_attribute, result=None):   

    if not result:
        result = dict()

    clustering_data = extract_clustering_data(df, class_attribute)

    model = KMeans(n_clusters=2)

    y_pred = model.fit_predict(clustering_data)
    
    print('\n----- KMeans Clustering -----\n')

    result['kmeans'] = evaluate_clustering(df.copy(), class_attribute, y_pred)

    return result


def implement_agglomerative(df, class_attribute, result=None):

    if not result:
        result = dict()

    clustering_data = extract_clustering_data(df, class_attribute)

    model = AgglomerativeClustering(n_clusters=2)

    y_pred = model.fit_predict(clustering_data)
    
    print('\n----- Agglomerative Clustering -----\n')

    result['agglomerative'] = evaluate_clustering(df.copy(), class_attribute, y_pred)

    return result


def implement_spectral(df, class_attribute, result=None):

    if not result:
        result = dict()

    clustering_data = extract_clustering_data(df, class_attribute)

    model = SpectralClustering(n_clusters=2)

    y_pred = model.fit_predict(clustering_data)
    
    print('\n----- Spectral Clustering -----\n')

    result['spectral'] = evaluate_clustering(df.copy(), class_attribute, y_pred)

    return result


def implement_birch(df, class_attribute, result=None):

    if not result:
        result = dict()

    clustering_data = extract_clustering_data(df, class_attribute)

    model = Birch(n_clusters=2)

    y_pred = model.fit_predict(clustering_data)
    
    print('\n----- Birch Clustering -----\n')

    result['birch'] = evaluate_clustering(df.copy(), class_attribute, y_pred)

    return result


def implement_all(df, class_attribute):

    result = dict()

    result = implement_kmeans(df.copy(), class_attribute, result)
    result = implement_agglomerative(df.copy(), class_attribute, result)
    result = implement_spectral(df.copy(), class_attribute, result)
    result = implement_birch(df.copy(), class_attribute, result)

    return result


