FROM python:3
ADD . /
RUN pip install requests
# CMD [ "python3","-m", "./veripy" ]
CMD [ "python3", "test-net.py" ]
