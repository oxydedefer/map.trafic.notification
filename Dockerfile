FROM python:3
ADD . /notification
WORKDIR /notification
RUN pip install -r requirements.txt
CMD ["python", "notification.py"]
