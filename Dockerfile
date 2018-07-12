FROM python:3
RUN mkdir -p /notification
ADD . /notification
WORKDIR /notification
RUN pip install -r requirements.txt
CMD ["python", "notification.py"]
