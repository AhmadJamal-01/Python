<!-- Create Virtual Environment  -->
conda create -n first_env pyhton=.10

<!-- Activate Environment -->
conda activate first_env

<!-- Deactivate Environment -->
conda deactivate

<!-- For Package Installation (pip & conda) -->
pip install numpay==2.2

<!-- Check all package install -->
conda list

<!-- check the environments information in your system -->
conda info -e

<!-- Delete the enviroment -->
conda remove --name first_env --all