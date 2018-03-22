## PDSB - Final Project Proposal
#### Alexander M. Procton

For my final project, I propose to create a Python package that will be able to convert sequential behavior data from focal animal sampling into a format for use in social network analysis.

__The problem:__ Animal behavior data is often recorded using the technique of focal animal sampling (FAS), in which a single individual is followed by an observer for a period of time (either a predetermined value, or from the onset of sampling until a specific behavior is observed). While the focal individual is  being observed, its behavior is noted at regular intervals ("beeps"). If some beeps include social behavior with another identified individual, these records of dyadic interactions can be combined to estimate the social network for a group.

I will write a package that includes a FAS class which is able to take as input a data frame of FAS records with identified individuals. When a user calls a function to pass one or more columns which contain records of interactions with other identified individuals, the object will return an igraph network object representing the recorded social behavior. The user will also be able to indicate if the network should be weighted or unweighted and directed or undirected. The FAS object will also be able to provide statistics about the FAS data, such as the mean and standard deviation of the number of beeps during which individuals were followed.

Other functionality I would like to implement, time permitting:

* Ability to merge multiple data frames, without double-counting repeat observations
* Graphics functionality, probably through toyplot.
* More advanced ways to define network ties e.g. combining multiple social behaviors

__The data:__ I will use a subset of the data that I'm using for my MA thesis with Marina Cords. The data will come from one group of blue monkeys (_Cercopithecus mitis_) living in Kakamega Forest, Kenya, with all subjects and all partners anonymized. If there is some issue making this data public, I will simulate comparable demo data.

__The tools:__ I decided to use igraph because I am familiar with this package in R, and it is one of the most widely used Python and R network packages. I will probably use toyplot because it works well with notebooks.

This project will accomplish the same thing as several functions that I wrote in R for my MA data. However, this tool is intended to work with generic sequential focal data, as long as there is a column identifying recorded interactions with other focal individuals.

__The novelty:__ To my knowledge, there is no currently existing Python or R package that can create networks from this type of data (or even sociomatrices or edgelists that can be read by most network software like igraph). R package asnipe (Farine 2013) offers related functionality in that it can construct social networks from co-occurence records, a distinctly different procedure for estimating social networks from serial data.

__The goal:__ By the due date, I will create an installable Python package that can be used to convert sequential FAS data into igraph objects. Hopefully I will also have time to implement some of the other functions I have thought of.


#### References

1. Csardi, G., & Nepusz, T. (2006). The igraph software package for complex network research. InterJournal, Complex Systems, 1695(5), 1-9.
2. Farine, D. R. (2013). Animal social network inference and permutations for ecologists in R using asnipe. Methods in Ecology and Evolution, 4(12), 1187-1194.
