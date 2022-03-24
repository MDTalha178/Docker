FROM python:3
ENV PYTHON UNBUFFERED  
WORKDIR / Drive 
COPY requirements.txt / Drive/
RUN pip install -r requirements.txt
COPY . / Drive/