FROM python:3
ENV PYTHONUNBUFFERED 1
EXPOSE 8080
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app
CMD python app.py


