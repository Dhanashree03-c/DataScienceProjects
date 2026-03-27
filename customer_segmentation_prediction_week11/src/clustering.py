"""
Customer clustering module.

Performs:
- feature scaling
- KMeans clustering
- hierarchical clustering
- DBSCAN clustering
- PCA visualization
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.decomposition import PCA

from utils import RANDOM_STATE, OPTIMAL_CLUSTERS, ensure_directory

# Scale features for clustering
def scale_features(df: pd.DataFrame):

    X = df.drop("Churn", axis=1)

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X, X_scaled


def apply_clustering(df: pd.DataFrame, X_scaled):

    df = df.copy()

    kmeans = KMeans(
        n_clusters=OPTIMAL_CLUSTERS,
        random_state=RANDOM_STATE
    )

    df["Cluster_KMeans"] = kmeans.fit_predict(X_scaled)

    hierarchical = AgglomerativeClustering(
        n_clusters=OPTIMAL_CLUSTERS
    )

    df["Cluster_Hierarchical"] = hierarchical.fit_predict(X_scaled)

    dbscan = DBSCAN(eps=0.8, min_samples=5)

    df["Cluster_DBSCAN"] = dbscan.fit_predict(X_scaled)

    return df


def visualize_clusters_pca(df, X_scaled,
                           output_path="../results/pca_clusters.png"):

    ensure_directory("../results")

    pca = PCA(n_components=2, random_state=RANDOM_STATE)

    pca_data = pca.fit_transform(X_scaled)

    df["PCA1"] = pca_data[:, 0]
    df["PCA2"] = pca_data[:, 1]

    plt.figure(figsize=(7,5))

    sns.scatterplot(
        data=df,
        x="PCA1",
        y="PCA2",
        hue="Cluster_KMeans",
        palette="Set2"
    )

    plt.title("Customer Segments (PCA Projection)")

    plt.tight_layout()

    plt.savefig(output_path)

    plt.show()

    print(f"PCA visualization saved to {output_path}")