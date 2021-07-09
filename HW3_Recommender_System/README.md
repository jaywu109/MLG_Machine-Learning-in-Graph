# HW3

The goal of HW3 is to build ***Recommender System*** on 3 datasets.  
In this project, we will implement classic algorithm from the basic Collaborative Filtering to state-of-the-art deep learning approach on three datasets. Besides, with the help of Graph Neural Network (GNN), a combined method has proposed in this project. In the following sections, for each of method used, we will go through how they work and discuss their strengths and weaknesses.

## Propsed Method
We propose a refine method to integrate a GNN based method Graph Convolutional Matrix Completion (GCMC) with DIFMs.  
![image](https://user-images.githubusercontent.com/36630295/125028123-08234480-e0ba-11eb-9db7-da2d976c5530.png)
The core idea of GCMC is to encode the original user-item rating matrix into a user and item embedding by formulating rating matrix as a bipartite graph. To obtain the predicted rating in GCMC, a Bilinear decoder followed by the application of a softmax function is shown as follows:  
![image](https://user-images.githubusercontent.com/36630295/125028216-399c1000-e0ba-11eb-8bfc-6426aeab61e7.png)
Consider the process of predicting in GCMC can be treated as another form of inn-product operation on the user and item embedding, we propose to incorporate the obtained user and item embedding in GCMC in Prediction Layer of DIFMs, which user and item embedding can be considered as features containing more expressive topology information while the FM in Prediction Layer allows it to combine user and item embedding with other features obtained in previous layer together.

## Experiment Result
![image](https://user-images.githubusercontent.com/36630295/125028285-56384800-e0ba-11eb-9834-97c8ac4f8e9c.png)
