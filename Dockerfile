FROM python:3.7-alpine
#FROM python:3.8.2

COPY ./conf.yaml /app/
COPY ./requirements.txt /app/
COPY ./setup.py /app/
COPY ./goldenduck/ /app/goldenduck/

WORKDIR /app/

RUN pip3 install -U setuptools
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install minepy
RUN pip3 install -r requirements.txt

#CMD ["sleep", "10000"]
CMD ["python3", "goldenduck/corplist.py"]
