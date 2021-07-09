# HW1

Implementation of DrBC, a novel graph neural network approach of learning to identify high betweenness centrality nodes

---
Betweenness centrality measures the number of times a node lies on the shortest path between other nodes. This measure shows which nodes are ‘bridges’ between nodes in a network. It does this by identifying all the shortest paths and then counting how many times each node falls on one. Nodes with high betweenness may have considerable influence within a network by virtue of their control over information passing between others.  For example, in a telecommunications network, a node with higher betweenness centrality would have more control over the network, because more information will pass through that node. It also applies to a wide range of problems in network theory, including problems related to social networks, biology, transport and scientific cooperation.


## Architecture of DrBC
![image](https://user-images.githubusercontent.com/36630295/125026424-23d91b80-e0b7-11eb-803c-775ad28bc7df.png)
