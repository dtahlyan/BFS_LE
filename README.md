[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


### NOTE
I am still updating this repo with the necessary content. This note will disappear when the repo is ready. While the example data to demostrate the code is not in the data folder yet, the code.py is ready and works perfectly. Feel free to clone this repo to start playing around. If you have any questions, please write to me at dtahlyan [AT] u [DOT] northwestern [DOT] EDU. 

# Breadth-First-Search Link Elimination (BFS-LE)
This repository contains python implementation of the modified breadth first search link elimination algorithm used for generating route choice sets in a network. The algorithm was originally proposed by [Rieser-Schussler et al. (2013)](https://www.tandfonline.com/doi/full/10.1080/18128602.2012.671383). The modified version, which generates *unique* routes instead of just routes, was proposed in my thesis and can be accessed [here](https://scholarcommons.usf.edu/etd/7649/). An augmented version of my thesis is expected to be out as a paper soon and is co-authored with [Prof. Abdul Pinjari](https://abdulpinjari.weebly.com/). The pre-print of the paper can be accessed [here](https://abdulpinjari.weebly.com/uploads/9/6/7/8/9678119/tahlyan_pinjari_route_choicesets_march_2018.pdf). 

The main code for used for the choice set generation can be found in ```code.py``` file. An example network, and the output from the code are presented in the ```data``` and ```generated_files``` folders, respectively. 

## EXAMPLE DATASET

The example network contains 500 nodes and 12,385 links and has been visualized below. This network was randomly generated using a link occurance probability of 0.05. 

![Alt text](images/sample_graph.png?raw=true "Visualization showing the example network")

Add content here


## REFERENCES 

If you find BFS_LE useful, please cite my [thesis](https://scholarcommons.usf.edu/etd/7649/). Thank you!
```
@article{tahlyan2018performance,
  title={Performance Evaluation of Choice Set Generation Algorithms for Modeling Truck Route 
  Choice: Insights from Large Streams of Truck-GPS Data},
  author={Tahlyan, Divyakant},
  year={2018}
}
```

Please also cite the original [paper](https://www.tandfonline.com/doi/full/10.1080/18128602.2012.671383) that proposed the BFS_LE algorithm. 
```
@article{rieser2013route,
  title={Route choice sets for very high-resolution data},
  author={Rieser-Sch{\"u}ssler, Nadine and Balmer, Michael and Axhausen, Kay W},
  journal={Transportmetrica A: Transport Science},
  volume={9},
  number={9},
  pages={825--845},
  year={2013},
  publisher={Taylor \& Francis}
}
```
