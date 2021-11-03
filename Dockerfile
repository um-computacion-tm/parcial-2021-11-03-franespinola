FROM python:3

RUN git clone https://github.com/um-computacion-tm/parcial-2021-11-03-franespinola.git

WORKDIR /parcial-2021-11-03-franespinola

CMD ["python", "./test_buscaminas.py"]