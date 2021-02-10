FROM dextra.dna/selenium-base:homolog

ENV APP_DIR=/usr/src/app

WORKDIR $APP_DIR

COPY requirements.txt ./

RUN apt-get install -y git

RUN pip install --no-cache-dir cryptography && \
    pip install -r requirements.txt 

RUN apt-get remove --purge -y git

CMD ["python", "main.py"]