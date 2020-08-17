FROM python:3.6.9

COPY ./requirements.txt /
RUN pip install -r requirements.txt
COPY ./goldenduck/corplist.py /

CMD ["python", "corplist.py"]
