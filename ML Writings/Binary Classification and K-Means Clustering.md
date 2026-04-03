# Binary Classification in Predictive Modeling and Clustering Methods Through K-Means

*By Claude Cordon Pichilla*

## Classification

Let us look at a simple example to understand where classification accuracy fails:

**Table 1**

*Disease Prediction Results*

| Patient ID | Has Disease? (True) |  | Has Disease? (Predicted) |
| :---: | :---: | :---: | :---: |
| **1001** | **Yes** |  | **No** |
| **1002** | **No** |  | **No** |
| **1003** | **No** |  | **No** |
| **1004** | **No** |  | **No** |
| **1005** | **No** |  | **No** |
| **1006** | **Yes** |  | **No** |
| **1007** | **No** |  | **No** |
| **1008** | **No** |  | **No** |
| **1009** | **No** |  | **No** |
| **1010** | **No** |  | **No** |
| **Accuracy** |  | **8/10** |  |

*Note:* This is an example of misleading accuracy with majority class prediction.

This is a bad model as it always predicts the majority class, but its high accuracy can trick us into thinking that the model is performing well. Since accuracy does not always show us the full picture, we can use a confusion matrix instead to tell us how well the model is actually performing. Based on above data and assumption, answer the following questions: 

**Table 2**

*Confusion Matrix*

|  | Has disease (Predicted) | No disease (Predicted) |  Total |
| :---: | :---: | :---: | :---: |
| Has disease (Actual) | True Positive TP \= 0 | False Negative FN \= 2 |  2 |
| No disease **(Actual)** | False Positive FP \= 0 | True Negative TN \= 8 |  8 |
| Total | 0 | 10 |  |

**True Positive (TP), False Positive (FP), True Negative (TN), False Negative (FN), Precision, Recall, and F1-score.**

Let us look at these values and then consider them in the context of patient data.

TP \= 0,	FP \= 0,	TN \= 8,	FN \= 2

Precision=TPTP+FP=00+0= 0

Recall=TPTP+FN=00+2=0

F1=2×precision×recallprecision+recall=2000+0= 0

According to the patient data in Table 1, there are 10 total patients. Having a disease is classified as the positive value the model is attempting to identify, and having no disease as the negative value. Out of 10 patients, two have a disease, and the other eight have no disease. 

True Positive(TP) indicates the number of times that the model correctly predicts a patient as having a disease, whereas False Positive(FP) values reflect the number of patients with no disease that the model has incorrectly identified as having a disease. 

True Negative(TN) is scored as the number of patients correctly identified as having no disease, and False Negatives(FN) as those incorrectly identified patients with a disease as having no disease. The overall ability to recall 

Precision is a value that is measured by the model correctly classifying a number of patients with a disease out of its total positive predictions (TP/(TP \+ FP). Recall measures the rate of the model to correctly detect these patients against its combined TP and *FN* score (TP/(TP \+ FN). In this dataset however, there were no positive outcomes identified either correctly or incorrectly (Table 2), which indicates a 0% True Positive Rate and therefore no precision or recall of these values. The F1 score is a measure of the models precision and recall (2\*(precision\*recall)/(precision \+ recall)) between  0 and 1\. F1 scores closer to 0 indicate the model’s favourability towards precision detection, whereas a score closer to 1 would lean toward recall. While the model’s F1 score being zero would likely suggest it is better at precision, it never predicted a disease in the patients, leaving the score relatively unusable.

**Although this model has an 80% accuracy, can we say there is something wrong with it by just looking at its confusion matrix?**

Given the inability of the model to make any positive predictions, and predicting all 10 patients as having  no disease, the confusion matrix in Table 2 displays a clear imbalance in favour of detecting Negatives. The given 80% accuracy reflects on its recall well if the goal of the model is not to identify a disease in the majority of patients. 

**If accuracy is not the proper metric, what metric can be the dominant one to measure how the model is actually performing?**

Discounting the option of increasing the size of the dataset, or running the model through further trials, I would suggest using the recall rate. By displaying the score as ‘0/2’ it can represent a minimum score that the model can improve upon. Accurately detecting one of the two patients, against the sum of both TP and FN shows where the model can improve. 

## K-Means Clustering

Consider a dataset of customer transactions in an e-commerce platform. Each transaction has two features: the amount spent, and the number of items purchased. We want to cluster these transactions into meaningful groups using the K-Means algorithm.

**Table 3**

*Customer Transactions and Spending*

| Transaction | Amount Spent($) | Items Purchased |
| :---: | :---: | :---: |
| 1 | 20 | 3 |
| 2 | 25 | 4 |
| 3 | 30 | 5 |
| 4 | 15 | 2 |
| 5 | 10 | 1 |
| 6 | 40 | 6 |
| 7 | 35 | 5 |
| 8 | 5 | 1 |
| 9 | 22 | 3 |
| 10 | 18 | 2 |

**a) Apply the K-Means algorithm to cluster the transactions into k=3 clusters. Use the initial centroids \[15, 2\], \[25, 4\], \[35, 5\].**

**Table 4**

*Iteration of K-Means with Initial Centroids*

|  |  | C1 | C2 | C3 |  |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  |  | \[15, 2\] | \[25, 4\] | \[35, 5\] |  |
| Transaction No. | Point | Dist. Mean 1 | Dist. Mean 2 | Dist. Mean 3 | Cluster |
| 1 | \[20, 3\] | 5.10 | 5.10 | 15.13 | 1, 2 |
| 2 | \[25, 4\] | 10.20 | 0 | 10.05 | 2 |
| 3 | \[30, 5\] | 15.30 | 5.10 | 5 | 3 |
| 4 | \[15, 2\] | 0 | 10.20 | 20.22 | 1 |
| 5 | \[10, 1\] | 5.10 | 15.30 | 25.32 | 1 |
| 6 | \[40, 6\] | 25.32 | 15.13 | 5.10 | 3 |
| 7 | \[35, 5\] | 20.22 | 10.05 | 0 | 3 |
| 8 | \[5, 1\] | 10.05 | 20.22 | 30.27 | 1 |
| 9 | \[22, 3\] | 7.07 | 3.16 | 13.15 | 2 |
| 10 | \[18, 2\] | 3 | 7.28 | 17.26 | 1 |

*Note.* Mean Euclidean distance from each centroid is calculated using p(a, b) \= sqrt((x2 – x1)2 \+ (y2 – y1)2), where a \= Amount spent per transaction, and b \= Number of items bought.

**Table 5**

*New Centers of Soft-Clustered(S) and Hard-Clustered(H) Data*

| Cluster 1(S) | Cluster 2(S) | Cluster 3(S) |  |  |  |  |  | Cluster 1(H) | Cluster 2(H) | Cluster 3(H) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| \[20,3\]\* \[15,2\] \[10,1\] \[5,1\] \[18,2\] | \[20,3\]\* \[22,3\] | \[30,5\] \[40,6\] \[35,5\] |  |  |  |  |  | \[15,2\] \[10,1\] \[5,1\] \[18,2\] | \[20,3\] \[22,3\] | \[30,5\] \[40,6\] \[35,5\] |
| C1 | C2 | C3 |  |  |  |  |  | C1 | C2 | C3 |
| **\[13.6, 2\]\*** | **\[21, 3\]** | **\[35, 5.3\]** |  |  |  |  |  | **\[12, 1.5\]\*** | **\[21, 3\]** | **\[35, 5.3\]** |

*Note.* \[20,3\] is included in both Cluster 1(S) and Cluster 2(S) as the overlap in soft-clustering, whereas in the hard-clustered data this data point is specifically moved to Cluster 2(H) for the purpose of highlighting the effect on variability in C1.

**b) What is the iteration stopping criteria of K-means algorithm? Based on the above data, how many iterations are optimal?** 

The ideal stopping point is found once there are notably clear partitions of similarity among a predefined number of clusters. If we were to use the hard-clustered centers found in Table 5, one further iteration would be sufficient in organizing the clusters. If using the calculations with soft-clustered means, two iterations at most will have sorted the data.

**c) Discuss how the K-Means algorithm's performance might be affected when dealing with a significantly larger dataset.** 

K-Means is a form of partitioning data based on a number of clusters provided by the user over a number of iterations in O(n) time complexity. K-Means is meant to partition data by without any overlap (hard clusters) where no data point can appear in multiple clusters, I chose to include it in my clustering analysis of the small Customer Transaction dataset (Table 3\) as an indication of where it may incorrectly partition data if not given enough iterations. Large datasets can be efficiently sorted, but he initial centroids used to determine the closeness between points are computed at random, which does not guarantee an exact set of clustered data every time the algorithm is initiated. Even if the dataset is large, if the type of data it clusters has wide discrepancy in the variability of clusters or an overrepresentation of data, it can be prone to inaccurate clustering. The user may have to initialize a different number of clusters or scale the frequency of other datapoints for consistency, or consider different methods to account for factors like noise and outliers.

**d) Explain how the presence of a transaction \[1000, 20\] in the dataset can impact the results of the K-Means clustering algorithm. You don’t need to calculate every step, show one and describe.**

The distances between \[1000, 20\] and each cluster is 985.16 \[15, 2\], 975.13 \[25, 4\], and 965.12 \[35, 5\].

A datapoint with an extreme value as \[1000, 20\] stands out as an outlier in the data, and the distance from this point and the initial centers, disproportionately skews the next mean of any of the initial clusters it would fall under.  The distance alone is not reflective of closeness to any of the given clusters.
