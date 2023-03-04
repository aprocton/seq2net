# seq2net
## A Python library for converting sequential data to social networks
Author: Alex Procton

Last updated: 3/3/2023

#### About
seq2net is a Python library that includes the SequentialData class, which is able to take as input any sequentially recorded behavioral data. The resulting object can then output networks as adjacency matrices or as ipython Graph objects.

#### Installation
Clone this repo and use pip to install seq2net.
```bash
git clone https://github.com/aprocton/seq2net.git
cd project/seq2net/
pip install .
```

#### How to use
seq2net provides an API for use in ipython notebooks and similar reproducible applications. See the notebook [`seq2net-demo.ipynb`](./notebooks/seq2net-demo.ipynb) for a detailed demonstration.

seq2net uses igraph for Python to create social networks. If you would like to visualize social networks using the igraph plot function, you will also need to install the Python bindings for the cairo graphics library separately (precompiled binaries for various operating systems/Python versions are available [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo))