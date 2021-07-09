# HW2

The goal of HW2 is to deal with Link Predcition Problem on 3 datasets.
One of major problem in the graph data that we are curious is link prediction. Link prediction is to predict whether two nodes in a network are likely to have a link(edge). In in a social network graph, we may want to know if there exist friendship links among users, while interactions between genes and proteins can be formulated as a link prediction problem in biological network graph.
The combination of Node2Vec and Graph AutoEncoder is adopted.

## Node2Vec
![image](https://user-images.githubusercontent.com/36630295/125026945-107a8000-e0b8-11eb-9379-af17b3447729.png)
![image](https://user-images.githubusercontent.com/36630295/125026951-12444380-e0b8-11eb-8cdb-92f0f20df722.png)

## Graph AutoEncoder
![image](https://user-images.githubusercontent.com/36630295/125027014-25571380-e0b8-11eb-85f9-44e115a37a7e.png)
![image](https://user-images.githubusercontent.com/36630295/125027023-28520400-e0b8-11eb-9df3-0752a16ddb23.png)

### Graph Convolutional Networks as Encoder in GAE
![image](https://user-images.githubusercontent.com/36630295/125027086-428be200-e0b8-11eb-8f75-da8d03ce665f.png)
![image](https://user-images.githubusercontent.com/36630295/125027094-4586d280-e0b8-11eb-9843-59ba6a6d72c6.png)
![image](https://user-images.githubusercontent.com/36630295/125027100-47e92c80-e0b8-11eb-966d-ec31b2e7f4c2.png)
The node embedding relationship between two layers can be expressed as the following formula:
![image](https://user-images.githubusercontent.com/36630295/125027120-520b2b00-e0b8-11eb-97d9-c879be9163b6.png)

