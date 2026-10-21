# Use the following commands to install the environment in your respective OS

Prerequisite: miniconda3 installed in your system.
If not, use the link: https://www.anaconda.com/download/success?reg=skipped-miniconda
and install it in your system. 

Use the installed specific to your system OS: Windows or Linux

## For Windows OS:

### Installation: 
1) Use the file "mlba_v1.yml" to create the conda environment in your system.
2) Use the following command to install the environment:

conda env create -f mlba_v1.yml

#### NOTE:  You need to be in the same directory while installing the env, 
otherwise give the entire path to the file like:

conda env create -f c:/to/the/path/mlba_v1.yml

Your environment will be installed.

### Activating conda env:

Use the following command to activate the mlba_v1 environment:

conda activate mlba_v1

Use the following command to deactivate the mlba_v1 environment:

conda deactivate


## For Linux OS:

### Installation: 
1) Use the file "mlba_v1_linux.yml" to create the conda environment in your system.
2) Use the following command to install the environment:

conda env create -f mlba_v1_linux.yml

#### NOTE:  You need to be in the same directory while installing the env, 
otherwise give the entire path to the file like:

conda env create -f c:/to/the/path/mlba_v1.yml

Your environment will be installed.

### Activating conda env:

Use the following command to activate the mlba_v1 environment:

conda activate mlba_v1

Use the following command to deactivate the mlba_v1 environment:

conda deactivate
