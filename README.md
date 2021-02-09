# Datathon IM - fev.2021
Repositório destinado a reunir todos os trabalhos feitos durante o Datathon Inteligência de Mercado do time DnA da Dextra que ocorreu do dia 8 a 12 de fevereiro de 2021.

## Build image base of Selenium

```bash
cd devops/selenium-docker-image && docker build -t dextra.dna/selenium-base:homolog .
cd ../..
```

## Run

```bash
# running mode deamon
docker-compose up -d
```
