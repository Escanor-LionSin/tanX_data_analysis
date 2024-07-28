FROM python:3.9

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
#Default behaviour is to run the script
CMD ["python", "code/script.py"]