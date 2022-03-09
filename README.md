# Pioneer Journalism Network Analysis
This repository contains all code, data and project files to gather and conduct Twitter network analysis and visualization via Gephi.  

### Prerequisites

1. Python
2. Gephi
3. Virtualenv

## Development
### Getting started
```bash
pip3 install -r requirements.txt
```

### Get user data via Twitter API
```bash
export TWITTER_BEARER_TOKEN=[your_token_here]
pip3 install -r requirements.txt
jupyterlab
```

### Data preparation
```bash
jupyterlab # then load up convert.ipynb
```

### Analysis with Gephi
After running your own collection OR using the data contained in this repository, you have nodes and edges sitting comfortably in `/csv`. Load these into the data laboratory in Gephi and visualize away.
   
### Copyright
(c) Leibniz HBI, Hamburg 2022
