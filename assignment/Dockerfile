FROM python:3.4

ADD hardware.xlsx /

ADD assignment.py /

RUN pip install xlrd
RUN pip install pandas


CMD [ "python", "./assignment.py" ]