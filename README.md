# Datathon IM - fev.2021
Repositório destinado a reunir todos os trabalhos feitos durante o Datathon Inteligência de Mercado do time DnA da Dextra que ocorreu do dia 8 a 12 de fevereiro de 2021.

## Created using Conda Env

- **Prerequisites**

    >[Install the conda Ubuntu 18.04 version to python 3.7](https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh)

    >[Install the conda Windows version to python 3.7](https://repo.anaconda.com/archive/Anaconda3-2020.02-Windows-x86_64.exe)

    >[Install the conda MacOS version to python 3.7](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html)


```bash
# reset environment conda, case it has already in your machine (OPTIONAL)
conda deactivate
conda remove -n datathon-dna --all

# creating 
create -n datathon-dna python==3.7.5 -y
conda activate datathon-dna

# install libs
pip install -r requirements.txt
```

## Using conda env with jupyter

```bash
ipython kernel install --user --name datathon-dna --display-name "Python (datathon-dna)"

# initialize jupyter
jupyter notebook --notebook-dir notebooks
```

## Build image base of Selenium

```bash
cd devops/selenium-docker-image && docker build -t dextra.dna/selenium-base:homolog .
cd ../..
```

## Run

```bash
export DYNACONF_HEADLESS=false && python dextra/dna/main.py
```

## Run with docker

```bash
# running mode deamon
docker-compose up -d
```
