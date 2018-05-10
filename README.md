# seq2net
## A Python library for converting sequential data to social networks
Author: Alex Procton

Last updated: 5/10/2018

#### About
seq2net is a Python library that includes the SequentialData class, which is able to take as input any sequentially recorded behavioral data. The resulting object can then output networks as adjacency matrices or as ipython Graph objects.

#### Installation
seq2net requires igraph for Python to create social networks. Installation instructions for python-igraph vary depending on your operating system and version of Python. To download igraph, please visit the [installation section](http://igraph.org/python/doc/tutorial/install.html#installing-igraph) of the python-igraph manual for detailed instructions. 

Windows users should download one of the binaries available from [this site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-igraph) and install using pip (i.e. `pip install FILENAME.whl`). Note that if you are using Windows, you will also need to install the Python bindings for cairo separately (also available [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo))

Clone this repo and use pip to install seq2net.
```bash
git clone https://github.com/aprocton/PDSB-project.git
cd PDSB-project/seqlib/
pip install .
```

#### How to use
seq2net provides an API for use in ipython notebooks and similar reproducible applications. See the notebook [`seq2net-demo.ipynb`](./notebooks/seq2net-demo.ipynb) for a detailed demonstration.