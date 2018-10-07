FROM python:3.4

ADD hardware.xlsx /

ADD a1.py /

RUN pip install xlrd
RUN pip install pandas


CMD [ "python", "./a1.py" ]