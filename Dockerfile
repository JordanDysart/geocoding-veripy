

FROM python:3
ADD . /
RUN pip install
CMD [ "python", "./src/handlefile.py" ]
