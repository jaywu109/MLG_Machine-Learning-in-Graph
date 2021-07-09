# Final Project

The goal of HW3 is to build a model to deal with ***Inductive Anomaly Detection with Missing Value***.  
Anomaly detection is an important task in machine learning, which is a task of identifying anomalies in a dataset. For example, the type of cancer instances is relatively rare compared to the normal instances in clinical data so it would often cause extremely data imbalance challenge. Other than medical domain, anomaly detection methods have been used in a wide variety of security-related applications such as financial fraud detection, social spam detection. Although many anomaly detection methods have been proposed in previous works, but there’s little attention specifically focused on dealing anomaly detection with missing values.  
In this project, we propose to deal with the anomaly detection task with existing missing value by the means of label prediction. Formulating the problem using a graph representation and applying Graph Neural Network(GNN), where we construct a bipartite graph with observations and features in tabular data as two types of nodes, and the observed feature values as attributed edges between the observation and feature nodes. Under this graph representation, the label anomaly prediction is treated as a node-level prediction task to classify whether a certain observation is normal or anomaly. 

## Method Used in Project
Formulating the missing value problem as a bipartite graph and introducing Graph Attention Network to refine thr process of aggregation.  
![image](https://user-images.githubusercontent.com/36630295/125028872-5127c880-e0bb-11eb-97ba-d033b71e69bc.png)  
![image](https://user-images.githubusercontent.com/36630295/125028930-6a307980-e0bb-11eb-9dea-3daafda7880e.png)  

---
Anomaly Detection of Attributed Graph with feature reconstruction and adjacency matrix reconstruction decoder.  
![image](https://user-images.githubusercontent.com/36630295/125029217-e5922b00-e0bb-11eb-9f71-bb8a0cefd62e.png)

---
Semi-supervised method by restricting the normal instance in certain space of hypersphere.  
![image](https://user-images.githubusercontent.com/36630295/125029364-18d4ba00-e0bc-11eb-8baf-7ab22f9baaef.png)

---
Incoporating GAN to train the generator of GAN to get a node embedding that is real enough to fool the discriminator. 
![image](https://user-images.githubusercontent.com/36630295/125029388-20945e80-e0bc-11eb-8f51-695844b53ae0.png)

## Experiment Result
The result without missing value is presented as baseline. In addition to the methods we’ve conducted in this project, 3 machine learning methods specific for anomaly detection are shown in this section as baseline.  
![image](https://user-images.githubusercontent.com/36630295/125029596-7ec14180-e0bc-11eb-947e-cc54a2b40fe1.png)  
To compare the result when missing value is appeared, we randomly choose 10% value of feature to become unobserved. 3 machine learning methods use MICE to complete imputation.  
![image](https://user-images.githubusercontent.com/36630295/125029611-85e84f80-e0bc-11eb-80ff-97694077dab1.png)
