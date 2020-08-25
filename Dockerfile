#FROM python:3.7-alpine
FROM python:3.8.2

COPY ./conf.yaml /app/
COPY ./requirements.txt /app/
COPY ./setup.py /app/
COPY ./goldenduck/ /app/goldenduck/

WORKDIR /app/

RUN python3 -m pip install --upgrade pip
RUN pip3 install wheel
RUN pip3 install setuptools 
RUN pip3 install -r requirements.txt
RUN python3 setup.py build
RUN python3 setup.py install

#CMD ["sleep", "1000"]
CMD ["python3", "goldenduck/corplist.py"]
