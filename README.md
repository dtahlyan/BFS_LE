[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.6](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)


# Breadth-First-Search Link Elimination (BFS-LE)
This repository contains python implementation of the modified breadth first search link elimination algorithm used for generating route choice sets in a network. The algorithm was originally proposed by [Rieser-Schussler et al. (2013)](https://www.tandfonline.com/doi/full/10.1080/18128602.2012.671383). The modified version, which generates *unique* routes instead of just routes, was proposed in my thesis and can be accessed [here](https://scholarcommons.usf.edu/etd/7649/). An augmented version of my thesis is now out as a paper and can be accessed [here](https://www.tandfonline.com/doi/full/10.1080/23249935.2020.1725790). 

The main code for used for the choice set generation can be found in ```code.py``` file. An example network (created using a random graph generation algorithm), and the output from the code for this network are presented in the ```data``` and ```generated_files``` folders, respectively. 

### REFERENCES 

If you find BFS_LE useful, please cite my the paper and my thesis. Thank you!

```
@article{tahlyanperformance,
  title={Performance Evaluation of Choice Set Generation Algorithms for Analyzing Truck Route Choice: Insights from Spatial Aggregation for the Breadth First Search Link Elimination (BFS-LE) Algorithm},
  author={Tahlyan, Divyakant and Pinjari, Abdul Rawoof}
  year={2020},
  journal={Transportmetrica A: Transport Science},
  publisher={Taylor \& Francis}
}
```


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
