FROM python:3
ADD . /
CMD [ "python3","-m", "./veripy" ]
