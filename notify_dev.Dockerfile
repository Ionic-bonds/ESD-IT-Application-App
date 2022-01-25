FROM python:3-slim
WORKDIR /usr/src/app
COPY amqp.reqs.txt http.reqs.txt ./
RUN pip install --no-cache-dir -r http.reqs.txt -r amqp.reqs.txt
COPY ./notify_dev.py ./invokes.py ./amqp_setup.py ./
CMD [ "python", "./notify_dev.py" ]
